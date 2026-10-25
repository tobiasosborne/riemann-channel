#define main trigonal_unused_main
#include "trigonal_search.cpp"
#undef main
int main(int argc,char**argv) {
    if(argc!=3)return 1;
    int e=stoi(argv[1]),b=stoi(argv[2]);
    vector<pair<int,int>> mons;
    for(int j=0;j<=4;j++)for(int i=0;i<=b-e*j;i++)mons.push_back({i,j});
    vector<vector<Point>> pts(9);
    for(int k=1;k<=8;k++)pts[k]=points(k,e,b,4);
    int targets[9]={0,3,5,2,7,6,9,18,18};
    for(int target:{3,5}) {
        targets[8]=target==3?18:34;
        for(int a=0;a<2;a++)for(int c=0;c<2;c++) {
            uint32_t offset=0;vector<uint32_t> basis;
            for(int i=0;i<int(mons.size());i++) {
                int xx=mons[i].first,yy=mons[i].second;
                if(xx+yy<2)continue;
                if(xx==1 && yy==1)offset|=1U<<i;
                else if(xx==2 && yy==0){if(a)offset|=1U<<i;}
                else if(xx==0 && yy==2){if(c)offset|=1U<<i;}
                else basis.push_back(1U<<i);
            }
            bool split=!(a&&c);vector<uint32_t> keep;uint32_t mask=offset;
            for(uint32_t i=0;i<(1U<<basis.size());i++) {
                if(i)mask^=basis[__builtin_ctz(i)];
                if(match(mask,pts[1],targets[1]-(split?1:-1)))keep.push_back(mask);
            }
            cout<<"TARGET "<<target<<" e "<<e<<" tangent "<<a<<" "<<c<<" dim "<<basis.size()<<" survivors "<<keep.size();
            for(int k=2;k<=8;k++) {
                int wanted=targets[k]-(k==2&&!split?1:0);vector<uint32_t> next;
                for(auto m:keep)if(match(m,pts[k],wanted))next.push_back(m);
                keep.swap(next);cout<<" "<<keep.size();
            }
            cout<<" MASKS";for(auto m:keep)cout<<" "<<m;cout<<endl;
        }
    }
}
