// Independent all-coefficient Dirichlet sums; no functional equation or Euler
// coefficient recursion. Affine orbits only avoid repeated, equivalent sums.
#include <array>
#include <vector>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <omp.h>
using namespace std;
using Poly=array<int,9>;
int q, d, pw[10], off[10], invv[16], eta[16], binom[10][10];
Poly decode(int code,int degree){Poly a{};for(int i=0;i<degree;i++){a[i]=code%q;code/=q;}a[degree]=1;return a;}
int encode(const Poly&a,int degree){int k=0;for(int i=degree-1;i>=0;i--)k=k*q+a[i];return k;}
int remainder(Poly&a,int da,const Poly&b,int db){
 for(int i=da;i>=db;i--){int c=a[i]*invv[b[db]]%q;
  for(int j=0;j<=db;j++)a[i-db+j]=(a[i-db+j]+q*q-c*b[j])%q;
 }
 da=min(da,db-1);while(da>=0&&!a[da])da--;return da;
}
bool squarefree(const Poly&a){Poly b{};for(int i=1;i<=d;i++)b[i-1]=i*a[i]%q;int db=d-1;while(db>=0&&!b[db])db--;Poly x=a;int dx=d;
 while(db>=0){dx=remainder(x,dx,b,db);swap(x,b);swap(dx,db);}return dx==0;}
int jacobi(Poly a,int da,Poly b,int db){int s=1;while(db>0){da=remainder(a,da,b,db);if(da<0)return 0;
 int lc=a[da];if(db%2)s*=eta[lc];int iv=invv[lc];for(int i=0;i<=da;i++)a[i]=a[i]*iv%q;
 if(q%4==3&&(da*db)%2)s=-s;swap(a,b);swap(da,db);
 }return s;}
int affine(const Poly&D,int b,int c){Poly E{};int bp[10]={1},cp[10]={1};for(int i=1;i<=d;i++){bp[i]=bp[i-1]*b%q;cp[i]=cp[i-1]*c%q;}
 for(int j=0;j<=d;j++)for(int k=0;k<=j;k++)E[k]=(E[k]+D[j]*binom[j][k]*bp[k]*cp[j-k])%q;
 int norm=invv[bp[d]];for(int k=0;k<=d;k++)E[k]=E[k]*norm%q;return encode(E,d);}
struct Orbit{int code,weight,oddweight;};
int main(int argc,char**argv){q=argc>1?stoi(argv[1]):7;d=argc>2?stoi(argv[2]):7;pw[0]=1;for(int i=1;i<=d;i++)pw[i]=pw[i-1]*q;
 eta[0]=0;for(int x=1;x<q;x++){for(int y=1;y<q;y++)if(x*y%q==1)invv[x]=y;eta[x]=-1;}for(int x=1;x<q;x++)eta[x*x%q]=1;
 for(int n=0;n<=d;n++){binom[n][0]=binom[n][n]=1;for(int k=1;k<n;k++)binom[n][k]=(binom[n-1][k-1]+binom[n-1][k])%q;}
 vector<char>seen(pw[d]);vector<Orbit>orbits;long long count=0;
 for(int code=0;code<pw[d];code++){if(seen[code])continue;auto D=decode(code,d);if(!squarefree(D)){seen[code]=1;continue;}
 vector<pair<int,int>>ims;for(int b=1;b<q;b++)for(int c=0;c<q;c++)ims.push_back({affine(D,b,c),eta[b]});sort(ims.begin(),ims.end());
 int weight=0,odd=0,last=-1;for(auto [im,s]:ims)if(im!=last){last=im;seen[im]=1;weight++;odd+=s;}orbits.push_back({code,weight,odd});count+=weight;
 }assert(count==pw[d]-pw[d-1]);cout<<"q="<<q<<" d="<<d<<" H="<<count<<" affine_orbits="<<orbits.size()<<endl;
 off[0]=0;for(int n=1;n<=d;n++)off[n]=off[n-1]+pw[n-1];int total=off[d];
 vector<Poly>ps(total);vector<int>degrees(total),factor(total,-1),quot(total,-1);
 for(int n=0;n<d;n++)for(int c=0;c<pw[n];c++){ps[off[n]+c]=decode(c,n);degrees[off[n]+c]=n;}
 for(int r=1;2*r<d;r++)for(int c=0;c<pw[r];c++){int pi=off[r]+c;if(factor[pi]>=0)continue;
  for(int s=r;s+r<d;s++)for(int a=0;a<pw[s];a++){int ai=off[s]+a;Poly m{};
   for(int i=0;i<=r;i++)for(int j=0;j<=s;j++)m[i+j]=(m[i+j]+ps[pi][i]*ps[ai][j])%q;
   int idx=off[r+s]+encode(m,r+s);if(factor[idx]<0){factor[idx]=pi;quot[idx]=ai;}
  }
 }
 vector<long long>sum(d);long long checked=0;int badfe=0;
 #pragma omp parallel
 {vector<int8_t>chars(total);vector<long long>local(d);int localbad=0;
 #pragma omp for schedule(dynamic,8)
 for(size_t j=0;j<orbits.size();j++){auto O=orbits[j];auto D=decode(O.code,d);chars[0]=1;vector<long long>coef(d);coef[0]=1;
  for(int idx=1;idx<total;idx++){int v=factor[idx]<0?jacobi(ps[idx],degrees[idx],D,d):chars[factor[idx]]*chars[quot[idx]];chars[idx]=v;coef[degrees[idx]]+=v;}
  for(int n=0;n<d;n++)local[n]+=coef[n]*(n%2?O.oddweight:O.weight);
  // FE is only a posterior consistency assertion, never used to construct a coefficient.
  int g=(d-1)/2;for(int n=0;n<g;n++)if(coef[2*g-n]!=pw[g-n]*coef[n])localbad++;
 }
 #pragma omp critical
 {for(int n=0;n<d;n++)sum[n]+=local[n];badfe+=localbad;}
 }
 cout<<"direct_sums=";for(auto s:sum)cout<<s<<",";cout<<"\naverage=";for(auto s:sum){long long k=gcd(abs(s),count);cout<<s/k<<"/"<<count/k<<",";}cout<<"\nposterior_FE_failures="<<badfe<<endl;assert(!badfe);
}
