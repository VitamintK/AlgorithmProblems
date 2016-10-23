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
	ll t;
	cin >> t;
	ll p, s, n;
	for(ll i = 0; i < t; i++){
		cin >> p >> s >> n;
		ll a;
		vector<ll> q;
		vector<ll> lru;
		ll qn = 0;
		ll lrun = 0;
		for(ll j = 0; j < n; j++){
			cin >> a;
			a = a/s;
			//queue
			bool inq = false;
			for(auto d: q){
				if(d == a){
					inq = true;
				}
			}
			if(!inq){
				q.push_back(a);
			}
			if(q.size() > p){
				q.erase(q.begin());
				qn++;
			}
			//lru
			auto asdf = find(lru.begin(), lru.end(), a);
			if(asdf != lru.end()){
				lru.erase(asdf);
				lru.push_back(a);
			} else {
				lru.push_back(a);
			}
			if(lru.size() > p){
				lru.erase(lru.begin());
				lrun++;
			}
		}
		if(lrun < qn){
			cout << "yes " << qn << " " << lrun << endl;
		} else {
			cout << "no " << qn << " " << lrun << endl;
		}
	}
}