#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	ll maxx = -1;
	cin >> n;
	vector<ll> as(n);
	for(ll i = 0; i < n; i++){
		cin >> as[i];
		maxx = max(maxx, as[i]);
	}
	ll ans = 0;
	for(ll i = 0; i < n; i++){
		ans += maxx - as[i]; 
	}
	cout << ans;
	return 0;
}