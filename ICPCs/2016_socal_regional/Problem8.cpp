#include <bits/stdc++.h>

#define REP(i,a,b) for(int i = (a); i < b; i++)
typedef long long ll;
using namespace std;
//THIS IS NOT THE OPTIMAL SOLUTION, BUT IT PASSED BECAUSE of the 60 second time limit. (very long)

int main(){
	ll n, k;
	cin >> n >> k;
	vector<ll> dp(10001,-1);
	vector<ll> prev(10001, -1);
	prev[0] = 0;
	vector<ll> ps(n);
	ll summ = 0;
	for(ll i = 0; i < n; i++){
		cin >> ps[i];
		summ+= ps[i];
	}
	for(ll i = 0; i < n; i++){
		//cout << "i " << i << endl;
		fill(dp.begin(), dp.end(), -1);

		for(ll k_owned = 0; k_owned <= i;k_owned++){
			//cout << prev[k_owned] << endl;
			if(prev[k_owned] > -1){
			if(k_owned >= k){
				dp[k_owned-k] = max(dp[k_owned-k], prev[k_owned] + ps[i]);
			}
			dp[k_owned+1] = max(dp[k_owned+1], prev[k_owned]);
			}
		}
		//for(ll p = 0; p < n; p++){
			//cout << dp[p] << endl;
		//}
		prev = dp;
	}
	ll best_savings = 0;
	for(ll i = 0; i < n; i++){
		//cout << dp[i] << endl;
		best_savings =  max(best_savings, prev[i]);
	}
	cout << summ - best_savings << endl;
}
