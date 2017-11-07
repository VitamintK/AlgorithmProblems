#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll n, k;
	cin >> n >> k;
	vector<pair<ll, ll>> pos;
	vector<pair<ll, ll>> neg;
	for(int i = 0; i < n; i++){
		ll x, m;
		cin >> x >> m;
		if(x > 0){
			pos.push_back(make_pair(x, m));
		} else {
			neg.push_back(make_pair(-x, m));
		}
	}
	sort(pos.begin(), pos.end());
	sort(neg.begin(), neg.end());
	reverse(pos.begin(), pos.end());
	reverse(neg.begin(), neg.end());
	ll ans = 0;
	ll have = 0;
//	ans += pos[0].first;
	for(int i = 0; i < pos.size(); i++){
		ll need = pos[i].second;
		ll dist = pos[i].first;
		if(have == 0){
			ans += 2*dist;
			have = k;
		}
		//cout << dist << " " << need << " " << have << endl;
		
		if(need > have){
			need -= have;
			ll trips = need/k;
			ans += trips * 2 * dist;
			need = need%k;
			have = 0;
			if(need > 0){
				ans += 2*dist;
				have = k;
			}
		}
		have = have - need;
		//assert need < k;
		
	}

	have = 0;
	
	for(int i = 0; i < neg.size(); i++){
		ll need = neg[i].second;
		ll dist = neg[i].first;
		if(have == 0){
			ans += 2*dist;
			have = k;
		}
		//cout << dist << " " << need << " " << have << endl;
		
		if(need > have){
			need -= have;
			ll trips = need/k;
			ans += trips * 2 * dist;
			need = need%k;
			have = 0;
			if(need > 0){
				ans += 2*dist;
				have = k;
			}
		}
		have = have - need;
		//assert need < k;
		
	}

	cout << ans << endl;
	return 0;
}