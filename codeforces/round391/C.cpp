#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n, m;
	cin >> n >> m;
	ll g;
	ll t;
	vector<vector<pair<ll,ll>>> holy(m); //row = type, stores pairs of (gym #, amount of that type)
	for(ll i = 0; i < n; i++){
		cin >> g;
		map<ll, ll> maaap;
		for(ll j = 0; j < g; j++){
			cin >> t;
			maaap[t]++;
		}
		for(auto k: maaap){
			holy[k.first-1].push_back(make_pair(i, k.second));
		}
	}
	sort(holy.begin(), holy.end());
	ll ans = 1;
	ll MOD = 1000000007;
	ll p = 1;
	for(ll i = 1; i < holy.size(); i++){
		if(holy[i-1] == holy[i]){
			p++;
			ans = (ans*p)%MOD;
		} else {
			p = 1;
		}
	}
	cout << ans;
	return 0;
}