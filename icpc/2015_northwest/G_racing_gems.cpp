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
std::ios_base::sync_with_stdio (false);

	ll n, r, w, h;
	while(cin >> n >> r >> w >> h){
	ll x, y;
	vector<pair<ll, ll>> coords;
	for(ll i = 0; i < n; i++){
		cin >> x >> y;
		coords.push_back(make_pair((y-(x*r)),(x*r + y)));
	}
	sort(coords.begin(), coords.end());
	// for(ll i = 0; i < n; i++){
	// 	cout << coords[i].first<< "," << coords[i].second << endl;
	// }
	//vector<vector<ll>> vectors;
	vector<ll> v;
	v.push_back(coords[0].second);
	//vectors.push_back(v);
	for (ll i = 1; i < n; i++){
		//vector<ll> copy = v;
		if(coords[i].second >= v[v.size()-1]){
			v.push_back(coords[i].second);
		} else if(coords[i].second < v[0]){
			v[0] = coords[i].second;
		} else {
			//if(*upper_bound(copy.begin(), copy.end(), coords[i].second) )
			*upper_bound(v.begin(), v.end(), coords[i].second) = coords[i].second;
		}
	}
	cout << v.size() << endl;
}
}