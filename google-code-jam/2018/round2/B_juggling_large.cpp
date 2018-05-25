#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	vector<vector<int>> DP(501, vector<int>(501));
	vector<vector<int>> DPp(501, vector<int>(501));

	vector<pair<int,int>> rbs; //List of all possible jugglers
	for(int i = 0; i < 35; i++){
		for(int j = 0; j < 35; j++){
			if(i>0 || j>0){
				rbs.push_back(make_pair(i,j));
			}
		}
	}

	//make the DP table
	for(int i = 0; i < rbs.size(); i++){
		int red = rbs[i].first;
		int blue = rbs[i].second;
		for(int j = 0; j < DP.size(); j++){
			for(int k = 0; k < DP[j].size(); k++){
				if(j-red >= 0 && k-blue>=0){
					DP[j][k] = max(DPp[j][k], DPp[j-red][k-blue]+1);
				} else {
					DP[j][k] = DPp[j][k];
				}
			}
		}

		for(int j = 0; j < DP.size(); j++){
			for(int k = 0; k < DP[j].size(); k++){
				DPp[j][k] = DP[j][k];
			}
		}

	}

	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		int r, b;
		cin >> r >> b;
		cout << "Case #" << t+1 << ": " << DP[r][b] << endl;
	}
	
	return 0;
}