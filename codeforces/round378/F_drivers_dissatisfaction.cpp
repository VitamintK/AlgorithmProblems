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
	ll n, m;
	cin >> n >> m;
	vector<vector<pair<ll, ll>> edges;
	vector<ll> weights(m);
	vector<ll> scalars(m);
	for(ll i = 0; i < m; i++){
		cin >> weights[i];
	}
	for(ll i = 0; i < m; i++){
		cin >> scalars[i];
	}
	ll a, b;
	vector<make_pair<ll,ll>> ref;
	for(ll i = 0; i < m; i++){
		cin >> a >> b;
		edges[a-1].push_back(make_pair(b-1, i));
		edges[b-1].push_back(make_pair(a-1, i));
		ref.push_back(make_pair(a-1, b-1));
	}
	ll s;
	cin >> s;
	//
	priority_queue<pair<ll, ll>> pq; //weight, (edge_id, )
	set<ll> tree;
	pq.push()
	while(!pq.empty()){

	}
}
