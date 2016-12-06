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
	ll n, x;
	cin >> n >> x;
	vector<ll> as(100001, 0);
	vector<ll> as2(n);
	ll a;
	for(ll i = 0; i < n; i++){
		cin >> as2[i];
		as[as2[i]]++;
	}
	ll ans = 0;
	for(ll i = 0; i < 100001; i++){
		ll targ = i ^ x;
		if(targ <= 100000){
			if(i == targ){
				ans+= as[i] * (as[i]-1);
			} else {
				ans+= as[i] * as[targ];
			}
		}
	}
	cout << ans/2 << endl;
	return 0;
}