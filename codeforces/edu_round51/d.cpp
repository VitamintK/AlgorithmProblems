#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <utility>

#define ll long long
#define ull unsigned long long
using namespace std;

ll MOD = 998244353;

int main(){
	std::ios::sync_with_stdio(false);
	int n,k;
	cin >> n >>k;

	vector<vector<ll>> dp(k+1, vector<ll>(4,0));
	vector<vector<ll>> pdp(k+1, vector<ll>(4,0));

	pdp[1][0] = 1;
	pdp[1][3] = 1;
	if(k > 1){
	pdp[2][1] = 1;
	pdp[2][2] = 1;
	}

	for(int i = 1; i < n; i++){
		//cout << "i: " << i << endl;
		for(int j = 1; j <= k; j++){
			dp[j][0]=pdp[j][0]  + pdp[j][1] + pdp[j][2] + pdp[j-1][3];
			dp[j][1]=pdp[j-1][0] + pdp[j][1] + pdp[j-1][3];
			if(j > 1){
				dp[j][1]+=pdp[j-2][2];
			}
			dp[j][2]=pdp[j-1][0] + pdp[j][2] + pdp[j-1][3];
			if(j > 1){
				dp[j][2]+=pdp[j-2][1];
			}
			dp[j][3]=pdp[j-1][0] + pdp[j][1] + pdp[j][2] + pdp[j][3];
			for(int kk = 0; kk < 4; kk++){
				dp[j][kk]%=MOD;
				// if(dp[j][kk] > 0){
				// 	cout << j << " " << kk << ": " << dp[j][kk] << endl;
				// }
			}
		}
		for(int j = 0; j <= k; j++){
			for(int m = 0; m < 4; m++){
				pdp[j][m] = dp[j][m];
			}
		}
	}

	cout << (pdp[k][0]+pdp[k][1]+pdp[k][2]+pdp[k][3])%MOD << endl;
	return 0;
}