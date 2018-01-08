#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int n;
	ll L;
	cin >> n >> L;
	vector<ll> costs(32, -1);
	for(int i = 0; i < n; i++){
		cin >> costs[i];
	}
	for(int i = 0; i < 32; i++){
		if(costs[i+1] == -1 || costs[i]*2 < costs[i+1]){
			costs[i+1] = costs[i]*2;
		}
	}
	
//to get 3, it might be better to get 4
//to get 3, it might be better to get 8
	ll ans = 0;
	for(int i = 0; i < costs.size(); i++){
		if(costs[i] < ans){
			ans = costs[i];
		}
		if((1 << i) & L){
			//cout << i << endl;
			ans += costs[i];
			//cout << costs[i] << endl;
		}
	}
	cout << ans << endl;
	return 0;
}