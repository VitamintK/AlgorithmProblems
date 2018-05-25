#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

bool FindMatch(int i, const vector<vector<int>> &w, vector<int> &mr, vector<int> &mc, vector<int> &seen){
	//copied from 1.5 Max Bipartite Matching from stanford notebook xD
	//https://cs.stanford.edu/group/acm/SLPC/notebook.pdf
	for(int j = 0; j < w[i].size(); j++){
		if(w[i][j] && !seen[j]){
			seen[j] = true;
			if(mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)){
				mr[i] = j;
				mc[j] = i;
				return true;
			}
		}
	}
	return false;
}

int BipartiteMatching(const vector<vector<int>> &w, vector<int> &mr, vector<int> &mc){
	mr = vector<int>(w.size(), -1);
	mc = vector<int>(w[0].size(), -1);

	int ct = 0;
	for(int i = 0; i < w.size(); i++){
		vector<int> seen(w[0].size());
		if(FindMatch(i, w, mr, mc, seen)){
			ct++;
		}
	}
	return ct;
}

int main(){
	std::ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		int N;
		cin >> N;
		vector<vector<int>> board(N, vector<int>(N));

		vector<vector<vector<int>>> bipartite_graphs(N+N+1, vector<vector<int>>(N, vector<int>(N)));
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				int color;
				cin >> color;
				board[i][j] = color;
				if(color >= 0){
					bipartite_graphs[color][i][j] = 1;
				} else{
					bipartite_graphs[N-color][i][j] = 1;
				}
			}
		}
		int ans = 0;
		for(int i = 0; i < bipartite_graphs.size(); i++){
			vector<int> temp1;
			vector<int> temp2;
			ans+=BipartiteMatching(bipartite_graphs[i], temp1, temp2);
			//cout << "after " << i << ": " << ans << endl;
		}


		cout << "Case #" << t+1 << ": " << N*N-ans << endl;
	}
	
	return 0;
}