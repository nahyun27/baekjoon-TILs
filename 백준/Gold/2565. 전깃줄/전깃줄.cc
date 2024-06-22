#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
 
int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
    
  int n,length = 0;
  cin>>n;
  
  vector<pair<int, int>> v;
  int dp[501]={0};
  
  for(int i=0;i<n;i++){
    int a, b;
    cin >> a >> b;
    v.push_back({a, b});
  }
  sort(v.begin(), v.end());

  dp[0]=1;

  for(int i = 1; i < n; i++){
      dp[i]=1; 
      for(int j = 0; j < i; j++){
          if(v[i].second > v[j].second){
              dp[i]=max(dp[j]+1, dp[i]);
          }
      }
      length = max(length, dp[i]);
  }
  
  cout << n-length << endl;
  return 0;
}