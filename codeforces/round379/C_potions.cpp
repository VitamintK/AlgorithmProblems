#include <bits/stdc++.h>

#define ll long long
using namespace std;

int main(){
	ll n, m, k;
	cin >> n >> m >> k;
	ll x, s;
	cin >> x >> s;
	//ll p1 = 0;
	ll pt = k-1;
	vector<ll> ms(m);
	vector<ll> ms_mana(m);
	vector<ll> ks(k);
	vector<ll> ks_mana(k);
	for(ll i = 0; i < m; i++){
		cin >> ms[i];
	}
	for(ll i = 0; i < m; i++){
		cin >> ms_mana[i];
	}
	vector<pair<ll,ll>> to_sort;
	for(ll i = 0; i < m; i++){
		to_sort.push_back(make_pair(ms_mana[i], ms[i]));
	}
	sort(to_sort.begin(), to_sort.end());
	for(ll i = 0; i < k; i++){
		cin >> ks[i];
	}
	for(ll i = 0; i < k; i++){
		cin >> ks_mana[i];
	}
	ll ans = n*x;
	while(ks_mana[pt] > s && pt >= 0){
			pt--;
	}
	if(pt >= 0){
		ans = min(ans, max(0ll,(n-ks[pt]))*x);
	}
	for(ll i = 0; i < m; i++){
		while(ks_mana[pt] + to_sort[i].first > s && pt >= 0){
			pt--;
		}
		if(pt < 0){
			if(to_sort[i].first <= s){
				ans = min(ans, (n)*to_sort[i].second);
				//cout << n << " " << to_sort[i].second << " " << ans << endl;
			}
		} else {
			ans = min(ans, (max(0ll,n-ks[pt]))*to_sort[i].second);
			//cout << n << " " << ks[pt] << " " << to_sort[i].second << " " << ans << endl;
		}
	}
	cout << ans << endl;
}