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
	ll p;
	cin >> p;
	ll r[501];
	ll g[501];
	ll bots[501];
	for(ll i = 0; i < p; i++){
		ll k, n;
		cin >> k >> n;
		for(ll j = 0; j < n; j++){
			cin >> r[j];
		}
		for(ll j = 0; j < n; j++){
			cin >> g[j];
		}
		for(ll j = 0; j < n; j++){
			bots[j] = j;
		}
		
		if(flag){
			cout << k << " NO" << endl;
		} else {
			cout << k << " YES" << endl;
		}
	}
}