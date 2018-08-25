#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

vector<int> colors;
vector<vector<int> > edges;

int dfs(int v, int color){
	//check if the graph is bipartite.
	
	//if a neighbor is the same color as this, then it's not bipartite
	for(int i = 0; i < edges[v].size(); i++){
		if(colors[edges[v][i]] == color){
			return false;
		}
	}
	colors[v] = color;
	//if a neighbor isn't colored yet, then recursively color it.
	for(int i = 0; i < edges[v].size(); i++){
		if(colors[edges[v][i]] == -1){
			if(!dfs(edges[v][i], 1-color)){
				return false;
			}
		}
	}
	return true;
}

int main(){
	std::ios::sync_with_stdio(false);
	int V;
	cin >> V;

	while(V != 0){
		colors.resize(V);
		edges.resize(V);
		edges.clear();
		for(int i = 0; i < V; i++){
			colors[i] = -1;
		}
		
		int a,b;
		cin >> a >> b;
		while(a!=0 && b!=0){
			a--; b--;
			edges[a].push_back(b);
			edges[b].push_back(a);
			cin >> a >> b;
		}
		if(dfs(0, 0)){
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
		}
		cin >> V;
	}
	return 0;
}