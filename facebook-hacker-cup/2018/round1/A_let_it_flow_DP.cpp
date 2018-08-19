#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		int n;
		cin >> n;
		vector<vector<int> > house(3, vector<int>(n));

		for(int i = 0; i < 3; i++){
			for(int j = 0; j < n; j++){
				char c;
				cin >> c;
				if(c == '.'){
					house[i][j] = 1;
				} else {
					house[i][j] = 0;
				}
			}
		}

		vector<int> DP = {1,0,0};
		vector<int> newDP = {0,0,0};
		for(int i = 0; i < n; i++){
			if(house[0][i] && house[1][i]){
				newDP[1]+=DP[0];
				newDP[0]+=DP[1];
			}
			if(house[1][i] && house[2][i]){
				newDP[2]+=DP[1];
				newDP[1]+=DP[2];
			}

			for(int j = 0; j < 3; j++){
				DP[j] = newDP[j]%1000000007;
				newDP[j] = 0;
			}
		}
		cout << "Case #" << t+1 << ": " << DP[2] << endl; 
	}
	return 0;
}