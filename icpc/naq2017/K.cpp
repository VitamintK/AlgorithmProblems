#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n, k, t1, t2;
	cin >> n >> k >> t1 >> t2;
	vector<ll> measurements(n);
	for(ll i = 0; i < n; i++){
		cin >> measurements[i];
	}
	ll l, r;
	vector<pair<ll, ll> > intervals;
	for(ll i = 0; i < k; i++){
		cin >> l >> r;
		intervals.push_back(make_pair(l, r));
	}
	vector<pair<ll, ll> > no_good;
	for(ll i = 0; i < k; i++){
		for(ll j = 0; j < n; j++){
			no_good.push_back(make_pair(intervals[i].first - measurements[j], intervals[i].second - measurements[j]));
		}
	}
	sort(no_good.begin(), no_good.end());
	vector<pair<ll, ll> > stack;
	stack.push_back(no_good[0]);
	for(ll i = 0; i < no_good.size(); i++){
		if(no_good[i].first <= stack.back().second){
			pair<ll, ll> x = stack.back();
			stack.pop_back();
			stack.push_back(make_pair(x.first, max(x.second, no_good[i].second)));
		} else {
			stack.push_back(no_good[i]);
		}
	}
	ll ans = 0;
	for(ll i = 0; i < stack.size(); i++){
		ll start = stack[i].first;
		ll end = stack[i].second;
		start = max(start, t1);
		end = min(end, t2);
		if(end > start){
		ans += (end - start);
		//cout << start << " to " << end << " is not OK" << endl;
		}
	}
	cout << setprecision(8) << 1 - (double)ans/(t2-t1) << endl;
	return 0;
}