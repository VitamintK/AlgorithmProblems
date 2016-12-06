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
	ll n, m, w;
	cin >> n >> m >> w;
	vector<vector<ll>> groups;
	vector<ll> weights(n);
	vector<ll> beauties(n);
	for(ll i = 0; i < n; i++){
		cin >> weights[i];
	}
	for(ll i = 0; i < n; i++){
		cin >> beauties[i];
	}
	vector<vector<ll>> edges(n);
	ll x, y;
	for(ll i = 0; i < m; i++){
		cin >> x >> y;
		edges[x-1].push_back(y-1);
		edges[y-1].push_back(x-1);
	}
	//cout <<"getting cc" << endl;
	//get connected components
	vector<ll> coloring(n, 0);
	ll color = 1;
	for(ll i = 0; i < n; i++){
		if(coloring[i] == 0){
			vector<ll> group;
			vector<ll> stack;
			stack.push_back(i);
			while(!stack.empty()){
				ll ex = stack.back();
				stack.pop_back();
				if(coloring[ex] == 0){
					group.push_back(ex);
				}
				coloring[ex] = color;
				for(ll i = 0; i < edges[ex].size(); i++){
					if(coloring[edges[ex][i]] == 0){
						stack.push_back(edges[ex][i]);
					}
				}
			}
			groups.push_back(group);
			color++;
		}
	}
	//
	//cout <<"starting dp" << endl;
	vector<ll> dp(w+1);
	for(ll i = 0; i < groups.size(); i++){
		//cout << i << endl;
		vector<ll> dp_old = dp;
		ll total_weight = 0;
		ll total_beauty = 0;
		for(ll j = 0; j < groups[i].size(); j++){
			ll index = groups[i][j];
			total_weight += weights[index];
			total_beauty += beauties[index];
			for(ll ww = 0; ww < w+1; ww++){
				if( ww >= weights[index]){
					dp[ww] = max(dp[ww], dp_old[ww-weights[index]] + beauties[index]);
				}
			}
		}

		for(ll ww = 0; ww < w+1; ww++){
			if( ww >= total_weight){
				dp[ww] = max(dp[ww], dp_old[ww-total_weight] + total_beauty);
			}
		}
	}
	cout << dp[w] << endl;
	return 0;
}