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
	ll n;
	cin >> n;
	ll a, b, c;
	map<pair<ll, ll>, pair<ll,ll>> m;
	ll best_diam = 0;
	pair<ll, ll> ans;
	for(ll i = 0; i < n; i++){
		cin >> a >> b >> c;
		vector<ll> t = {a,b,c};
		sort(t.begin(), t.end());
		a = t[0]; b = t[1]; c = t[2];
		if(min(min(a,b),c) > best_diam){
			best_diam = min(min(a,b),c);
			ans = make_pair(-1, i+1);
		}
		if(min(min(m[make_pair(a, b)].first + c, b), a) > best_diam){
			best_diam = min(min(m[make_pair(a, b)].first + c, b), a);
			ans = make_pair(i+1, m[make_pair(a, b)].second+1);
		}
		if(min(min(m[make_pair(b, c)].first + a, b), c) > best_diam){
			best_diam = min(min(m[make_pair(b, c)].first + a, b), c);
			ans = make_pair(i+1, m[make_pair(b, c)].second+1);
		}
		if(min(min(m[make_pair(a, c)].first + b, a), c) > best_diam){
			best_diam = min(min(m[make_pair(a, c)].first + b, a), c);
			ans = make_pair(i+1, m[make_pair(a, c)].second+1);
		}
		m[make_pair(a, b)] = max(m[make_pair(a, b)], make_pair(c,i));
		m[make_pair(a, c)] = max(m[make_pair(a, c)], make_pair(b,i));
		m[make_pair(b, c)] = max(m[make_pair(b, c)], make_pair(a,i));
	}
	if(ans.first == -1){
		cout << 1 << endl << ans.second << endl;
	} else {
		cout << 2 << endl << ans.first << " " << ans.second << endl;
	}
}