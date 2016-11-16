#include <bits/stdc++.h>

#define REP(i,a,b) for(int i = (a); i < b; i++)
typedef long long ll;
using namespace std;

template <class T>
int to_int(T &s){
	int to_return;
	stringstream SS;
	SS << s;
	SS >> to_return;
	return to_return;
}

int E, V;
vector<int> adj[100001];
int dfs_low[100001];
int dfs_num[100001];
int visited[100001];
int dfsNumberCounter, numSCC;
vector<int> S;
vector<int> biggestResult;

void tarjanSCC(int u){
	dfs_low[u] = dfs_num[u] = dfsNumberCounter++;
	S.push_back(u);
	visited[u] = 1;
	REP(j, 0, (int)adj[u].size()){
		int v = adj[u][j];
		if (!dfs_num[v]){
			tarjanSCC(v);
		}
		
		if (visited[v]){
			dfs_low[u] = min(dfs_low[u], dfs_low[v]);
		}
	}
	
	vector<int> data;
	
	if (dfs_low[u] == dfs_num[u]){
		while(1){
			int v = S.back(); S.pop_back(); visited[v] = 0;
			data.push_back(v);

			if (u == v) break;
		}
		if (data.size() > biggestResult.size()) biggestResult = data;
	}
}
int main(){	
	int T;
	cin >> T;
	REP(t, 0, T){
		dfsNumberCounter = numSCC = 0;
		memset(dfs_low, 0, sizeof(dfs_low));
		memset(dfs_num, 0, sizeof(dfs_num));
		memset(visited, 0, sizeof(visited));
		biggestResult.clear();
		cin >> V >> E;
		fill(adj, adj+V, vector<int>());
		S.clear();
		int u,v;
		REP(e, 0, E){
			cin >> u >> v;
			adj[u].push_back(v);
		}
		
		tarjanSCC(0);
		if (biggestResult.size() == V){
			cout << "Gotta Catch Them All!\n";
		}
		else
			cout << "Oh, oh!\n";
	}
	
	return 0;
}


