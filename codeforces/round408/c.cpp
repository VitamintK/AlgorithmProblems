#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

vector<vector<ll>> edges;
vector<ll> strength;
ll ans = 1e11;
ll maxcost = -1e10;

ll dfs(ll r, ll parent, ll maxfromparent){
	//neighbor, semineighbor
	//cout << "starting dfs for " << r << endl;
	ll sncosts = -1e10;
	ll ncosts = -1e10;
	vector<ll> childcosts;
	vector<ll> prefixmax;
	vector<ll> suffixmax;
	for(ll i = 0; i < edges[r].size(); i++){
		if(edges[r][i] != parent){
			ll max_cost_of_strict_descendants_of_this_child = dfs(edges[r][i], r, -1e11);
			sncosts = max(max_cost_of_strict_descendants_of_this_child+2, sncosts);
			ncosts = max(ncosts, strength[edges[r][i]]+1);
			childcosts.push_back(max(strength[edges[r][i]], max_cost_of_strict_descendants_of_this_child));
		}
		else{
			childcosts.push_back(-1e11);
		}
	}
	prefixmax.resize(edges[r].size());
	suffixmax.resize(edges[r].size());
	prefixmax[0] = -1e10;
		for(ll i = 1; i < edges[r].size(); i++){
					if(edges[r][i] != parent){

				prefixmax[i] = max(prefixmax[i-1], childcosts[i-1]);
			}
		}
	suffixmax[edges[r].size() -1] = -1e10;
		for(ll i = (ll)edges[r].size() - 2; i >= 0; i--){
					if(edges[r][i] != parent){

				suffixmax[i] = max(suffixmax[i+1], childcosts[i+1]);
			}
		}
	
	if(maxfromparent != -1e11){
		for(ll i = 0; i < edges[r].size(); i++){
			if(edges[r][i] != parent){
				if(parent == -1){
					dfs(edges[r][i], r, max(max(suffixmax[i],prefixmax[i]),maxfromparent));
				} else {
					dfs(edges[r][i], r, max(max(max(suffixmax[i],prefixmax[i]),maxfromparent),strength[parent]));
				}
			}
		}
		ll myans;
		if(parent == -1){
			myans = max(max(max(sncosts, ncosts), strength[r]),maxfromparent+2);

		} else {
			myans = max(max(max(max(sncosts, ncosts), strength[r]),strength[parent]+1),maxfromparent+2);
		}
		ans = min(myans, ans);
		//cout << sncosts << " " << ncosts << " " << strength[r] << " " << strength[parent]+1 << " " << maxfromparent+2 << endl;
		//cout << "r: " << r << endl << "mmmm: " << myans << endl;

	}
	return max(ncosts-1, sncosts-2);
}

int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n;
	strength.resize(n);
	for(ll i = 0; i < n; i++){
		cin >> strength[i];
		maxcost = max(strength[i], maxcost);
	}
	edges.resize(n);
	for(ll i = 0; i < n-1; i++){
		ll u, v;
		cin >> u >> v;
		edges[u-1].push_back(v-1);
		edges[v-1].push_back(u-1);
	}
	dfs(0, -1, -1e10);
	cout << ans << endl;
	return 0;
}