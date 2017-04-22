#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n, m, k;
	cin >> n >> m >> k;
	vector<int> hs(n+1,0);
	for(ll i = 0; i < m; i++){
		ll h;
		cin >> h;
		hs[h] = 1;
	}
	ll bone_loc = 1;
	for(ll i = 0; i < k; i++){
		if(hs[bone_loc] == 1){
			break;
		}
		ll u, v;
		cin >> u >> v;
		if(u == bone_loc){
			bone_loc = v;
		} else if(v == bone_loc){
			bone_loc = u;
		}
		if(hs[bone_loc] == 1){
			break;
		}
	}
	cout << bone_loc << endl;
	return 0;
}