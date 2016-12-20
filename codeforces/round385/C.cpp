#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
#include <utility>
#define ll long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll n, m, k;
	cin >> n >> m >> k;
	vector<ll> ks(n);
	for(ll i = 0; i < k; i++){
		ll a;
		cin >> a;
		ks[a-1] = 1;//index by 0;
	}
	vector<vector<ll>> edges(n);
	for(ll i = 0; i < m; i++){
		ll u, v;
		cin >> u >> v;
		edges[u-1].push_back(v-1);
		edges[v-1].push_back(u-1);
	}
	vector<ll> discovered(n);
	vector<ll> government_size;
	ll non_g_total = 0;
	for(ll i = 0; i < n; i++){
		if(discovered[i] == 0){
			vector<ll> stack;
			stack.push_back(i);
			discovered[i] = 1;
			ll gov = false;
			ll size = 0;
			while(!stack.empty()){
				ll ex = stack.back();
				stack.pop_back();
				if(ks[ex] == 1){
					gov = true;
				}
				size++;
				for(ll j = 0; j < edges[ex].size(); j++){
					if(discovered[edges[ex][j]] == 0){
						stack.push_back(edges[ex][j]);
						discovered[edges[ex][j]] = 1;
					}
				}
			}
			if(gov){
				government_size.push_back(size);
			} else {
				non_g_total += size;
			}
		}
	}
	auto max_g = max_element(government_size.begin(), government_size.end());
	ll max_gg = *max_g;
	government_size.erase(max_g);
	ll ans = 0;
	//cout << "max_gg: " << max_gg << endl;
	for(ll i = 0; i < government_size.size(); i++){
	//	cout << government_size[i] << endl;
		//cout << "government size: " << government_size[i] << endl;
		//cout << "edges " << (government_size[i] * (government_size[i]-1))/2 << endl;
		ans+= (government_size[i] * (government_size[i]-1))/2;
	}
	//cout << "no goves: " << non_g_total << endl;
	max_gg+=non_g_total;
	ans += (max_gg * (max_gg -1))/2;
	//cout << "bigthing edges " << (max_gg * (max_gg -1))/2 << endl;
	//cout << "total edges " << ans << endl; 
	cout << ans - m;
	return 0;
}