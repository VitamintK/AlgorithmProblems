#include <bits/stdc++.h>

#define ll long long
using namespace std;

int main(){
	ll n;
	cin >> n;
	vector<ll> ns(n);
	for(ll i = 0; i < n; i++){
		cin >> ns[i];
	}
	vector<vector<ll>> edges(n);
	vector<pair<ll,ll>> stck;
	stck.push_back(make_pair(0,0));
	for(ll i = 0; i < n-1; i++){
		ll u, v;
		cin >> u >> v;
		edges[u-1].push_back(v-1);
		edges[v-1].push_back(u-1);
	}
	//cout <<"HEY" << endl;
	//to find the diameter of tree:  
	//first, do  DFS to find the "furthest" point from node 0 (where the distance = number of times the color changes during the path)
	set<ll> explored;
	explored.insert(0);
	ll furthest_dist = 0;
	ll furthest_node;
	while(!stck.empty()){
		pair<ll,ll> ex = stck.back();
		stck.pop_back();
		if(ex.first > furthest_dist){
			furthest_dist = ex.first;
			furthest_node = ex.second;
		}
		for(ll v = 0; v < edges[ex.second].size(); v++){
			if(explored.count(edges[ex.second][v]) < 1){
				explored.insert(edges[ex.second][v]);
				stck.push_back(make_pair(ex.first + ((ns[ex.second]==ns[edges[ex.second][v]])?0:1),edges[ex.second][v]));
			}
		}
	}
	//if it's all one color, the answer is 0 lol.
	if(furthest_dist == 0){
		cout << 0 << endl;
		return 0;
	}

	//second, do the same dfs starting from the "furthest" point that you found in the first dfs, and find _its_ furthest point.
	//the distance to that point is the diameter.

	stck.push_back(make_pair(0,furthest_node));
	explored.clear();
	 furthest_dist = 0;
	 explored.insert(furthest_node);
	//furthest_node;
	while(!stck.empty()){
			pair<ll,ll> ex = stck.back();

		 ex = stck.back();
		stck.pop_back();
		if(ex.first > furthest_dist){
			furthest_dist = ex.first;
			furthest_node = ex.second;
		}
		for(ll v = 0; v < edges[ex.second].size(); v++){
			if(explored.count(edges[ex.second][v]) < 1){
				explored.insert(edges[ex.second][v]);
				stck.push_back(make_pair(ex.first + ((ns[ex.second]==ns[edges[ex.second][v]])?0:1),edges[ex.second][v]));
			}
		}
	}

	//the answer to the question is a function of the diameter (copied from editorial)
	cout << (furthest_dist+1)/2 << endl;
}