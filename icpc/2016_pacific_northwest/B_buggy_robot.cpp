#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

typedef pair<int, pair<int, int>> state; //depth, changes, y, x

int main(){
	std::ios::sync_with_stdio(false);
	int n, m;
	cin >> n >> m;
	vector<vector<int>> grid(n, vector<int>(m));
	pair<int, int> R;
	pair<int, int> E;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			char c;
			cin >> c;
			if(c == 'R'){
				R = make_pair(i, j);
			}
			if(c == 'E'){
				E = make_pair(i, j);
			}
			if(c == '#'){
				grid[i][j] = 0;
			} else {
				grid[i][j] = 1;
			}
		}
	}
	map<char, pair<int, int>> directions;
	directions['L'] = make_pair(0, -1);
	directions['R'] = make_pair(0, 1);
	directions['U'] = make_pair(-1, 0);
	directions['D'] = make_pair(1, 0);
	string s;
	cin >> s;
	set<state> been;
	map<state, int> DP;
	queue<state> q;
	q.push(make_pair(0, R));
	DP[make_pair(0, R)] = 0;
	while(!q.empty()){
		state ex = q.front();
		//cout << "using " << ex.first << " at r:" << ex.second.first << " c:" << ex.second.second << " costs " << DP[ex] << endl; 
		q.pop();
		for(int dx = -1; dx <= 1; dx++){
			for(int dy = -1; dy <= 1; dy++){
				if((dx == 0 && dy == 0) || (dx!= 0 && dy != 0)){
					continue;
				}
				int ny = ex.second.first + dy;
				int nx = ex.second.second + dx;
				if(!(ny >= 0 && ny < n && nx >= 0 && nx < m && grid[ny][nx])){
					ny-=dy;
					nx-=dx;
				}
					if(ex.first < s.length() && make_pair(dy, dx) == directions[s[ex.first]]){
						if(DP.count(make_pair(ex.first+1, make_pair(ny, nx))) == 0){
							DP[make_pair(ex.first+1, make_pair(ny, nx))] = DP[ex];
							q.push(make_pair(ex.first+1, make_pair(ny, nx)));
						}
					} else {
						if(DP.count(make_pair(ex.first, make_pair(ny, nx))) == 0){
							DP[make_pair(ex.first, make_pair(ny, nx))] = DP[ex]+1;
							q.push(make_pair(ex.first, make_pair(ny, nx)));
						}
					}
			}
		}
	}
	int ans = 1000000;
	for(int i = 0; i <= s.length(); i++){
		if(DP.count(make_pair(i, E)) > 0){
			ans = min(ans, DP[make_pair(i, E)]);
		}
	}
	cout << ans << endl;
	return 0;
}