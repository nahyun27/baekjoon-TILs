#include <iostream>
#include <vector>

using namespace std;

int root, rem, leaf;
vector<int> tree[51];

void dfs (int node) {
  if (node == rem) return;
  if (!tree[node].size()) {
    leaf++;
    return;
  }
  for (int i = 0; i < tree[node].size(); i++){
    dfs(tree[node][i]);
    if (tree[node][i] == rem && tree[node].size() == 1)
      leaf++;
  }
  return;
}

int main() {
  int n;
  cin >> n;
  // 트리 만들기
  for(int i = 0; i < n; i++) {
    int parent;
    cin >> parent;
    if(parent == -1) {
      root = i;
    } else {
      tree[parent].push_back(i);
    }
  }
  cin >> rem;
  dfs(root);
  cout << leaf;
  return 0;
}