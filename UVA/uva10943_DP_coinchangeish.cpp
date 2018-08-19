#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int n, k;
	int MOD = 1000000;
	cin >> n >> k;
	while(n!=0 || k!= 0){
		vector<vector<int>> DP(k+1, vector<int>(101));
		//vector<int> newDP(100);
		DP[0][0] = 1;
			//DP[0][i] = 1;
		for(int l = 1; l <= k; l++){//l is the layer (cardinality of coins added to make the sum)
				
			for(int i = 0; i <= n; i++){//i is the coin denomination

				for(int j = 0; j<= n; j++){//j is the value of the sum
					if(j >= i){
						DP[l][j] += DP[l-1][j-i];
						DP[l][j]%=MOD;
					}
				}
			}
		}
		int ans = DP[k][n];
		
		cout << ans << endl;
		cin >> n >> k;
	}
	
	return 0;
}