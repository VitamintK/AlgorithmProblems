#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n;
	string s;
	cin >> s;
	vector<pair<ll, ll>> dp(s.length()+1, pair<ull,ll>(-1,-1)); //value, digits
	dp[s.length()] = make_pair(0,0);
	for(ll i = s.length()-1; i >= 0; i--){
		string digit = "";
		for(ll backtrack = 0; backtrack < 10; backtrack++){
			if(i+backtrack >= s.length()){
				break;
			}
			digit = digit + s[i+backtrack];
			if(digit[0] == '0' && backtrack > 0){ //no leading zeroes
				break;
			}
			//ll value = stoll(digit); lmao mingw doesn't work
			ll value = atoll(digit.c_str());
			//cout << value << endl;
			if(value >= n){
				break;
			}
			ull total_value = value * pow(n,dp[i+backtrack+1].second) + dp[i+backtrack+1].first;
			if(dp[i].second == -1 || dp[i+backtrack+1].second+1 < dp[i].second || (dp[i+backtrack+1].second+1 == dp[i].second && total_value < dp[i].first)){
				dp[i] = make_pair(total_value, dp[i+backtrack+1].second + 1);
			}
			//dp[i] is the minimum 
		}
	}
	//for(ll i = 0; i < s.length()+1; i++){
	//	cout << i << " " << dp[i].first << " " << dp[i].second << endl;
	//}
	cout << dp[0].first << endl;
	return 0;
}