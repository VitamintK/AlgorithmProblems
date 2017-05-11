#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n;
	vector<ll> prices(n);
	vector<int> front(n);
	vector<int> back(n);
	for(ll i = 0; i < n; i++){
		cin >> prices[i];
	}
	for(ll i = 0; i < n; i++){
		cin >> front[i];
	}
	for(ll i = 0; i < n; i++){
		cin >> back[i];
	}
	vector<pair<ll,pair<int, int>>> pfb(n);
	for(ll i = 0; i < n; i++){
		pfb[i] = make_pair(prices[i], make_pair(front[i], back[i]));
	}
	sort(pfb.begin(), pfb.end());
	ll m;
	cin >> m;
	vector<ll> pointers;
	pointers.push_back(0);
	pointers.push_back(0);
	pointers.push_back(0);
	pointers.push_back(0);

	int c;
	for(int i = 0; i < m; i++){
		cin >> c;
		while(pointers[c] < n && pfb[pointers[c]].second.second != c && pfb[pointers[c]].second.first != c){
			pointers[c]++;
		}
		if(pointers[c] >= n){
			cout << -1;
		} else {
			cout << pfb[pointers[c]].first;
			pfb[pointers[c]] = make_pair(0,make_pair(0,0));
		}
		cout << " ";
	}
	cout << endl;
	return 0;
}