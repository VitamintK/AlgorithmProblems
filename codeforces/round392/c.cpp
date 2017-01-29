#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n, m, k, x, y;
	cin >> n >> m >> k >> x >> y;
	ll cycle = (2*n - 2)*m;
	if(n == 1){
		cycle = m;
	}
	ll cycles = k/cycle;
	ll mids = cycles*2;
	ll ends = cycles;
	//ll ans_min = cycles;
	//if(k%cycle >= n*m){
	//	ans_min++;
	//}
	vector<vector<ll>> naive(n,vector<ll>(m, mids));
	for(ll i = 0; i < m; i++){
		naive[0][i] = ends;
		naive[n-1][i] = ends;
	}
	ll rk = k%cycle;
	ll ans_min = 8000000000000000000;
	ll ans_max = -1;
	for(ll i = 0; i < n && rk>0; i++){
		for(ll j = 0; j < m && rk>0; j++){
			naive[i][j]++;
			rk--;
		}
	}
	for(ll i = n-2; i > 0 && rk>0; i--){
		for(ll j = 0; j < m && rk>0; j++){
			naive[i][j]++;
			rk--;
		}
	}
	for(ll i = 0; i < n; i++){
		for(ll j = 0; j < m; j++){
			ans_min = min(ans_min, naive[i][j]);
			ans_max = max(ans_max, naive[i][j]);
		}
	}
	cout << ans_max << " " << ans_min << " " << naive[x-1][y-1] << endl;
	return 0;
}