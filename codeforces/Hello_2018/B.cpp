#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

vector<vector<int> > children;
vector<int> parent;

int dfs(int i){
	int num_of_leaves = 0;
	bool desc_val = true;
	if(children[i].size() == 0){
		return true;
	}
	for(int j = 0; j < children[i].size(); j++){
		if(children[children[i][j]].size() == 0){
			num_of_leaves++;
		} else {
			desc_val &= dfs(children[i][j]);
		}
	}
	return ((num_of_leaves >= 3) && (desc_val));
}

int main(){
	std::ios::sync_with_stdio(false);
	int n;
	cin >> n;
	children.resize(n);
	parent.resize(n);
	for(int i = 0; i < n-1; i++){
		int a;
		cin >> a;
		parent[i+1] = a-1;
		children[a-1].push_back(i+1);
	}
	if(dfs(0)){
		cout << "Yes" << endl;
	} else {
		cout << "No" << endl;
	}
	return 0;
}