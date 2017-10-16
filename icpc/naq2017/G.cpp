#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n;
	set<pair<ll,ll>> pointz;
	vector<ll> magicx = {0, 1118, 1680, 2018, 1680, 1118, 0, -1118, -1680, -2018, -1680, -1118};
	vector<ll> magicy = {2018, 1680, 1118, 0, -1118, -1680, -2018, -1680, -1118, 0, 1118, 1680};
	ll ans = 0;
	for(ll i = 0; i < n; i++){
		ll x, y;
		cin >> x >> y;
		for(int i = 0; i < 12; i++){
			if(pointz.count(make_pair(x + magicx[i], y + magicy[i])) > 0){
				ans+=1;
			}
		}
		pointz.insert(make_pair(x,y));
	}
	cout << ans;
	return 0;
}