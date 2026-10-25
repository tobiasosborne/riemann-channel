// Exact exhaustive search of binary equations on F_e.
// Called and compiled by genus8_search.py. All arithmetic is integral.
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
struct Point { array<uint32_t,12> rows{}; int rank=0; };
int mul(int a,int b,int q,int mod) {
    int c=0;
    while(b) { if(b&1)c^=a; b>>=1; a<<=1; if(a&q)a^=mod; }
    return c;
}
vector<Point> points(int k,int e,int b,int fiber_degree=3) {
    const int mods[]={0,3,7,11,19,37,67,131,285,529,1033,2053,4179};
    int q=1<<k,mod=mods[k];
    vector<int> sq(q+1);
    for(int x=0;x<q;x++)sq[x]=mul(x,x,q,mod);
    sq[q]=q;
    vector<bool> seen((q+1)*(q+1));
    vector<Point> out;
    for(int x=0;x<=q;x++)for(int y=0;y<=q;y++) {
        int key=x*(q+1)+y;
        if(seen[key])continue;
        int xx=x,yy=y,len=0;
        do { seen[xx*(q+1)+yy]=true; len++; xx=sq[xx]; yy=sq[yy]; }
        while(xx!=x || yy!=y);
        if(len!=k)continue;
        vector<int> xp(b+1,1),yp(fiber_degree+1,1);
        if(x<q)for(int i=1;i<=b;i++)xp[i]=mul(xp[i-1],x,q,mod);
        if(y<q)for(int j=1;j<=fiber_degree;j++)yp[j]=mul(yp[j-1],y,q,mod);
        array<uint32_t,12> raw{};
        int pos=0;
        for(int j=0;j<=fiber_degree;j++)for(int i=0;i<=b-e*j;i++,pos++) {
            int v=(x==q ? int(i==b-e*j) : xp[i]);
            v=mul(v,(y==q ? int(j==fiber_degree) : yp[j]),q,mod);
            for(int z=0;z<k;z++)if(v>>z&1)raw[z]|=uint32_t(1)<<pos;
        }
        Point pt;
        for(int z=0;z<k;z++) {
            uint32_t r=raw[z];
            for(int j=0;j<pt.rank;j++)r=min(r,r^pt.rows[j]);
            if(r) { pt.rows[pt.rank++]=r; sort(pt.rows.begin(),pt.rows.begin()+pt.rank,greater<uint32_t>()); }
        }
        out.push_back(pt);
    }
    return out;
}
bool match(uint32_t mask,const vector<Point>& pts,int target) {
    int n=0;
    for(const auto& pt:pts) {
        bool zero=true;
        for(int j=0;j<pt.rank;j++)if(__builtin_parity(mask&pt.rows[j])) {zero=false;break;}
        if(zero && ++n>target)return false;
    }
    return n==target;
}
int main(int argc,char**argv) {
    if(argc<4)return 1;
    int e=stoi(argv[1]),b=stoi(argv[2]),g=stoi(argv[3]);
    int dim=4*(b+1)-6*e;
    vector<int> targets;
    for(int j=4;j<argc;j++)targets.push_back(stoi(argv[j]));
    if(int(targets.size())!=g || dim>30)return 2;
    vector<uint32_t> keep;
    cout<<"F_"<<e<<" b="<<b<<" genus="<<g<<" dimension="<<dim<<" equations="<<(uint32_t(1)<<dim)<<endl;
    for(int k=1;k<=g;k++) {
        auto pts=points(k,e,b);
        vector<uint32_t> next;
        if(k==1) {
            for(uint32_t mask=0;mask<(uint32_t(1)<<dim);mask++)if(match(mask,pts,targets[k-1]))next.push_back(mask);
        } else {
            for(auto mask:keep)if(match(mask,pts,targets[k-1]))next.push_back(mask);
        }
        keep.swap(next);
        cout<<"k="<<k<<" surface_closed_points="<<pts.size()<<" target_a="<<targets[k-1]<<" survivors="<<keep.size()<<endl;
        if(keep.empty())break;
    }
    cout<<"FINAL_MASKS";
    for(auto m:keep)cout<<" "<<m;
    cout<<endl;
    return 0;
}
