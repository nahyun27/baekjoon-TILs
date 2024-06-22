#include <iostream>
using namespace std; 

long long seg[4000005], sz;

void construct(){
  for(int i = sz; i > 0; i--){
    seg[i] = seg[2 * i] + seg[2*i +1];
  }
}

void update(long long i, long long val){
  seg[i] = val;
  while(i > 1){
    i/=2;
    seg[i] = seg[i*2] + seg[i*2+1];
  }
}

// nL, nR : 현재 범위
long long sum(long long L, long long R, long long vtx, long long nL, long long nR){
  if(nR < L || R < nL) return 0;
  if(L <= nL && nR <= R) return seg[vtx];

  long long mid = (nL + nR)/2;
  return sum(L, R, vtx*2, nL, mid) + sum(L, R, vtx*2+1, mid+1, nR);
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);
  long long n, m, k;
  cin >> n >> m >> k;

  long long level = 1;
  while(sz < n){
    sz += level;
    level *= 2; 
  }
  for(int i = sz + 1; i <= sz + n; i++){
    cin >> seg[i];
  }
  construct();
  for(int i = 0; i < m + k; i++){
    long long  a, b, c;
    cin >> a >> b >> c;
    if (a == 1) {
      update(sz + b, c);
    } else if (a == 2) {
      // 상위 노드(1) 부터 시작
      cout << sum(b, c, 1, 1, level) << '\n';
    }
  }
}