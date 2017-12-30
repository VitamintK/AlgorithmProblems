#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll n, m, k;
	cin >> n >> m >> k;
	vector<int> day(1000000);
	for(ll i = 0; i < n; i++){
		int a;
		cin >> a;
		day[a-1] = 1;
	}
	ll count = 0;
	ll ans = 0;
	for(ll i = 0; i < 1000000; i++){
		if(day[i]){
			count++;
		}
		if(i-m >= 0 && day[i-m]==1){
			count--;
		}
		if(count >= k){
			ans++;
			count--;
			day[i] = 0;
		}
	}
	cout << ans << endl;
	return 0;
}