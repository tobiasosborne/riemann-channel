// Plane sextic search engine, using exact binary arithmetic from the trigonal engine.
#define main trigonal_unused_main
#include "trigonal_search.cpp"
#undef main
#include <fstream>
vector<array<int,3>> monomials() {
    vector<array<int,3>> out;
    for(int i=0;i<=6;i++)for(int j=0;j<=6-i;j++)out.push_back({i,j,6-i-j});
    return out;
}
vector<Point> plane_points(int k) {
    const int mods[]={0,3,7,11,19,37,67,131,285,529,1033};
    int q=1<<k,mod=mods[k];
    auto mons=monomials();vector<Point> out;
    vector<int> sq(q);
    for(int i=0;i<q;i++)sq[i]=mul(i,i,q,mod);
    for(int first=0;first<3;first++) {
        int size=first==0?q*q:first==1?q:1;
        vector<bool> seen(size);
        for(int idx=0;idx<size;idx++) {
            if(seen[idx])continue;
            array<int,3> pt={0,0,0};pt[first]=1;
            if(first==0) {pt[1]=idx/q;pt[2]=idx%q;}
            if(first==1)pt[2]=idx;
            auto cur=pt;int len=0;
            do {
                int key=first==0?cur[1]*q+cur[2]:first==1?cur[2]:0;
                seen[key]=true;len++;
                for(auto &a:cur)a=sq[a];
            }while(cur!=pt);
            if(len!=k)continue;
            int powers[3][7];
            for(int z=0;z<3;z++) {powers[z][0]=1;for(int i=1;i<=6;i++)powers[z][i]=mul(powers[z][i-1],pt[z],q,mod);}
            array<uint32_t,12> raw{};
            for(int i=0;i<int(mons.size());i++) {
                int v=1;
                for(int z=0;z<3;z++)v=mul(v,powers[z][mons[i][z]],q,mod);
                for(int z=0;z<k;z++)if(v>>z&1)raw[z]|=uint32_t(1)<<i;
            }
            Point rp;
            for(int z=0;z<k;z++) {
                uint32_t r=raw[z];
                for(int j=0;j<rp.rank;j++)r=min(r,r^rp.rows[j]);
                if(r){rp.rows[rp.rank++]=r;sort(rp.rows.begin(),rp.rows.begin()+rp.rank,greater<uint32_t>());}
            }
            out.push_back(rp);
        }
    }
    return out;
}
int main(int argc,char**argv) {
    if(argc!=2)return 1;
    ifstream inp(argv[1]);int cases,g;inp>>cases>>g;
    vector<vector<Point>> pts(g+1);
    for(int k=1;k<=g;k++)pts[k]=plane_points(k);
    for(int ci=0;ci<cases;ci++) {
        int id,dim;uint32_t offset;inp>>id>>dim>>offset;
        vector<uint32_t> basis(dim);
        for(auto &b:basis)inp>>b;
        int target[13];for(int k=1;k<=g;k++)inp>>target[k];
        vector<uint32_t> keep;
        uint32_t mask=offset;
        for(uint32_t i=0;i<(uint32_t(1)<<dim);i++) {
            if(i)mask^=basis[__builtin_ctz(i)];
            if(match(mask,pts[1],target[1]))keep.push_back(mask);
        }
        cout<<"CASE "<<id<<" dim "<<dim<<" survivors "<<keep.size();
        for(int k=2;k<=g;k++) {
            vector<uint32_t> next;
            for(auto m:keep)if(match(m,pts[k],target[k]))next.push_back(m);
            keep.swap(next);cout<<" "<<keep.size();
        }
        cout<<" MASKS";for(auto m:keep)cout<<" "<<m;
        cout<<endl;
    }
}
