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

ll do_thing(vector<vector<ll>>& children, vector<ll>& pleas, vector<ll>& sums, vector<ll>& best_ans, ll node){
	ll total = pleas[node];
	//cout << "TOTAL "  << total << endl;
	ll BA = -1e16;
	for(ll i = 0; i < children[node].size(); i++){
		total+=do_thing(children, pleas, sums, best_ans, children[node][i]);
		BA = max(BA, best_ans[children[node][i]]);
	}
	BA = max(BA, total);
	sums[node] = total;
	best_ans[node] = BA;
	//cout << BA << " BA" << endl;
	return total;
}

int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n;
	vector<ll> pleas(n);
	vector<vector<ll>> edges(n);
	for(ll i = 0; i < n; i++){
		cin >> pleas[i];
	}
	for(ll i = 0; i < n-1; i++){
		ll u, v;
		cin >> u >> v;
		edges[u-1].push_back(v-1);
		edges[v-1].push_back(u-1);
	}
	vector<ll> parent(n, -1);
	vector<vector<ll>> children(n);
	vector<ll> stack;
	stack.push_back(0);
	while(!stack.empty()){
		ll ex = stack.back();
		stack.pop_back();
		for(ll i = 0; i < edges[ex].size(); i++){
			if(edges[ex][i] != parent[ex]){
				parent[edges[ex][i]] = ex;
				children[ex].push_back(edges[ex][i]);
				stack.push_back(edges[ex][i]);
			}
		}
	}
	bool ok = false;
	for(ll i = 0; i < n; i++){
		if(children[i].size() > 1){
			ok = true;
		}
	}
	if(ok == false){
		cout <<"Impossible" << endl;
		return 0;
	}
	vector<ll> sums(n);
	vector<ll> best_ans(n);
	//cout <<"83'" << endl;
	do_thing(children, pleas, sums, best_ans, 0);
	for(ll i = 0; i < best_ans.size(); i++){
		//cout << best_ans[i] << " ";
	}
		//cout << endl;

	for(ll i = 0; i < n; i++){
		//cout << "children of " << i << ": ";
		for(ll j = 0; j < children[i].size(); j++){
			//cout << children[i][j] << " ";
		}
		//cout << endl;
	}
	//cout <<"85" << endl;
	ll best_2 = -1e16;
	for(ll i = 0; i < n; i++){
		ll a = -1e16;
		ll b = -1e16;
		for(ll j = 0; j < children[i].size(); j++){
			if(best_ans[children[i][j]] > a){
				b = a;
				a = best_ans[children[i][j]];
			} else {
				if(best_ans[children[i][j]] > b){
					b = best_ans[children[i][j]];
				}
			}
		}
		best_2 = max(best_2, a+b);
	}
	cout << best_2 << endl;
	return 0;
}