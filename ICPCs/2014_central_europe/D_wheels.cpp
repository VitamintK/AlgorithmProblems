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

ll gcd(ll a, ll b){
	if(b == 0){
		return a;
	} else {
		return gcd(b, a%b);
	}
}

int main(){
	ll T;
	cin >> T;
	ll xs[1001];
	ll ys[1001];
	ll rs[1001];
	for(ll t = 0; t < T; t++){
		ll n;
		cin >> n;
		for(ll i =0; i < n; i++){
			cin >> xs[i] >> ys[i] >> rs[i];
		}
		pair<ll,ll> rates[1001];
		fill(rates, rates+1001, pair<ll,ll>(0,0));
		rates[0] = make_pair(1,1);
		//ll wheel = 0;
		vector<ll> dfs;
		dfs.push_back(0);
		while(!dfs.empty()){
			ll wheel = dfs.back();
			dfs.pop_back();
			bool found_ans = false;
			for(ll i = 0; i < n; i++){
				if(rates[i].first == 0 && rates[i].second == 0 && i != wheel && 
				   (xs[i] - xs[wheel])*(xs[i] - xs[wheel]) + (ys[i]-ys[wheel])*(ys[i]-ys[wheel]) <= (rs[i] + rs[wheel])*(rs[i] + rs[wheel])) {
					//cout << wheel << " " << i << endl;
					ll n = abs(rs[wheel] * rates[wheel].first);
					ll d = abs(rs[i] * rates[wheel].second);
					ll GCD = gcd(n,d);
					n = n/GCD;
					d = d/GCD;
					if(rates[wheel].first < 0){
						rates[i] = make_pair(n,d);
					} else{
						rates[i] = make_pair(-1*n,d);
					}
					//wheel = i;
					//found_ans = true;
					dfs.push_back(i);
				}
			}
		}
		for(ll i = 0; i < n; i++){
			if(rates[i].second == 0){
				cout << "not moving" << endl;
				continue;
			} else if(rates[i].second == 1){
				cout << abs(rates[i].first) << " " << (rates[i].first > 0 ? "clockwise" : "counterclockwise") << endl;
				continue;
			} else{
				cout << abs(rates[i].first) << "/" << rates[i].second << " " << (rates[i].first > 0 ? "clockwise" : "counterclockwise") << endl;
				continue;
			}
		}
	}
}