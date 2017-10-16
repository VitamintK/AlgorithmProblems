#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	int n;
	cin >> n;
	vector<ll> coins(n);
	for(int i = 0; i < n; i++){
		cin >> coins[i];
	}

	vector<ll> dp(coins[n-1] + coins[n-2]); //dp[i] is the minimum numebr of coins needed to make $i
	dp[0] = 0;
	for(ll i = 1; i < coins[n-1] + coins[n-2]; i++){
		dp[i] = 12345678;
		for(int id = n-1; id >= 0; id--){
			ll coin_value = coins[id];
			if(coin_value > i){
				continue;
			}
			if(dp[i - coin_value]+1 < dp[i]){
				if(dp[i] != 12345678){
					cout << "non-canonical" << endl;
					return 0;
				}
				dp[i] = dp[i-coin_value]+1;
			}
		}
	}
	cout << "canonical" << endl;
	return 0;
}