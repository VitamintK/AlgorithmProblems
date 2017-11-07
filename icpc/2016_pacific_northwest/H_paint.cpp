#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

bool comparePairs(const pair<ll,ll>& lhs, const pair<ll, ll>& rhs){
	return lhs.second < rhs.second;
}

int main(){
	std::ios::sync_with_stdio(false);
	ll n, k;
	cin >> n >> k;
	vector<pair<ll, ll> > ints;
	map<ll, ll> ends;
	for(int i = 0; i < k; i++){
		ll a, b;
		cin >> a >> b;
		ints.push_back(make_pair(a, b));
		//ends[b] = 0;
	}
	sort(ints.begin(), ints.end(), comparePairs);
	ends[0] = 0;
	ll ans = 0;
	for(int i = 0; i < k; i++){
		//cout << ints[i].second << endl;
		auto b4_end = --ends.lower_bound(ints[i].second);
		auto b4_start = --ends.lower_bound(ints[i].first);
		ends[ints[i].second] = max(ends[ints[i].second],
			max(b4_end->second, b4_start->second + ints[i].second - ints[i].first + 1));
		ans = max(ans, ends[ints[i].second]);
	}
	cout << n - ans << endl;
	return 0;
}