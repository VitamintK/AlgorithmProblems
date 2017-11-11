#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	int n, m;
	vector<vector<int> > values;
	vector<vector<int> > DP;
	while(cin >> n >> m){
		values.clear();
		DP.clear();
		for(int i = 0; i < n; i++){
			values.push_back(vector<int>(m));
			DP.push_back(vector<int>(m));
			for(int j = 0; j < m; j++){
				cin >> values[i][j];
				if(i > 0){
					DP[i][j] = max(DP[i][j], DP[i-1][j]);
				}
				if(j > 0){
					DP[i][j] = max(DP[i][j], DP[i][j-1]);
				}
				DP[i][j] += values[i][j];
			}
			if(i > 0){
				cout << " ";
			}
			cout << DP[i][m-1];
		}
		cout << endl;
	}
	return 0;
}