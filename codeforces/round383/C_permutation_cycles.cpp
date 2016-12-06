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

int gcd(int a, int b) {
while (b) { int t = a%b; a = b; b = t; }
return a;
}

int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n;
	vector<ll> crushes(n, 0);
	set<ll> crushmap;
	for(ll i = 0; i < n; i++){
		cin >> crushes[i];
		crushes[i]--;
		if(crushmap.count(crushes[i]) > 0){
			cout << -1 << endl;
			return 0;
		}
		crushmap.insert(crushes[i]);
	}
	cout <<" " << endl;
	vector<ll> cycles;
	for(ll i = 0; i < n; i++){
		if(crushes[i] != 0){
			ll cylen = 1;
			ll index = crushes[i];
			while(index != i){
				//cout << index << endl;
				cylen++;
				ll xsa = index;
				index = crushes[index];
				crushes[xsa] = 0;
			}
			if(cylen%2 == 0){
				cylen = cylen/2;
			}
			cycles.push_back(cylen);
		}
	}
	ll gcd_ = cycles[0];
	ll prod = cycles[0];
	ll lcm = cycles[0];
	for(ll i = 1; i < cycles.size(); i++){
		gcd_ = gcd(lcm, cycles[i]);
		prod = lcm * cycles[i];
		lcm = prod/gcd_;
	}
	cout << lcm << endl;
	return 0;
}