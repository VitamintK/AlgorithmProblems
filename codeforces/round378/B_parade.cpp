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
	ll l, r;
	vector<ll> deltas;
	ll tot = 0;
	for(ll i = 0; i < n; i++){
		cin >> l >> r;
		tot+= r-l;
		deltas.push_back(2*l - 2*r);
	}
	ll ans = -1;
	ll ansaux = abs(tot);
	for(ll i = 0; i < n; i++){
		if(abs(tot+deltas[i]) > ansaux){
			ansaux = abs(tot+deltas[i]);
			ans = i;
		}
	}
	cout << ans+1 << endl;
}