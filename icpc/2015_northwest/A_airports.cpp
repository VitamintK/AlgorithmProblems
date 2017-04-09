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
typedef vector<ll> VI;
typedef vector<VI> VVI;
bool FindMatch(ll i, const VVI &w, VI &mr, VI &mc, VI &seen){
	for(ll j = 0; j < w[i].size(); j++){
		if(w[i][j] && !seen[j]){
			seen[j] = true;
			if(mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)){
				mr[i] = j;
				mc[j] = i;
				return true;
			}
		}
	}
	return false;
}

int main(){
	ll n, m;
	while(cin >> n >> m){
	//	cout << "here" << endl;
	vector<vector<ll>> times (n,vector<ll>(n, 0ll));
		vector<vector<ll>> shortest (n,vector<ll>(n, 0ll));

	ll a;
	for(ll i = 0; i < n; i++){
		cin >> a;
		for(ll j = 0; j < n; j++){
			if(j != i){
				times[j][i] = a;
			} else {
				times[j][i] = 0;
			}
		}
	}
	//cout <<"oh ok" << endl;
	 for(ll i = 0; i < n; i++){
	 	for(ll j = 0; j < n; j++){
	 		cin >> a;
	 		times[i][j] += a;
	 		shortest[i][j] = times[i][j];
	 	}
	 }
//stolen idea from judges' solution: since n,m < 500, we can use floyd-warshall (O(V^3)) which is fine
	 //otherwise do dijkstra's here
	 for(ll mid = 0; mid < n; mid++){
	 	for(ll start = 0; start < n; start++){
	 		for(ll end = 0; end < n; end++){
	 			if(shortest[start][end] > shortest[start][mid] + shortest[mid][end]){
	 				shortest[start][end] = shortest[start][mid] + shortest[mid][end];
	 			}
	 		}
	 	}
	 }
	vector<ll> ss(m, 0ll);
	vector<ll> fs(m, 0ll);
	vector<ll> starts(m, 011);
	vector<ll> ends(m, 011);
	ll s, f, t;
	//cout <<"72" << endl;
	for(ll i = 0; i < m; i++){
		cin >> s >> f >> t;
		s = s-1;
		f = f-1;
		ss[i] = s;
		fs[i] = f;
		starts[i] = t;
		ends[i] = t+times[s][f];
	}
	//cout <<"this line" << endl;
	//vector<vector<ll>> edges(n);
	//vector<vector<ll>> edges_to(n);
	vector<vector<ll>> w(m, vector<ll>(m, 0ll));
	for(ll flight = 0; flight < m; flight++){
		for(ll other = 0; other < m; other++){
			if(ends[flight] + shortest[fs[flight]][ss[other]]<= starts[other] && flight != other){
				//edges[flight].push_back(other);
				//edges_to[other].push_back(flight);
				w[flight][other] = 1;
				//cout << flight << " to " << other << endl;
			}
		}
	}
	VI mr = VI(m, -1ll);
	VI mc = VI(m, -1ll);
	ll ct = 0ll;
	for(ll i = 0ll; i < w.size(); i++){
		VI seen(m, 0ll);
		if(FindMatch(i,w,mr,mc,seen)){
			ct++;
		}
	}
	cout <<  m - ct << endl;
}
}