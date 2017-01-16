#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n;
	vector<ll> s(n);
	for(ll i = 0; i < n; i++){
		cin >> s[i];
	}
	map<ll, ll> factor_count;
	ll max_ans = 0;
	for(ll i = 0; i < n; i++){
		//cout << sqrt(s[i]) << endl;
		for(ll divisor = 2; divisor <= sqrt(s[i]); divisor++){
			if (s[i]%divisor == 0){
				factor_count[divisor]++;
				if(s[i]/divisor != divisor){
					factor_count[s[i]/divisor]++;
				}
				max_ans = max({factor_count[divisor], factor_count[s[i]/divisor], max_ans});
			}
		}
		if(s[i] != 1){
			factor_count[s[i]]++;
			max_ans = max(max_ans, factor_count[s[i]]);
		}
	}
	cout << max(max_ans,1ll);
	return 0;
}