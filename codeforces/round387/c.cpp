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
	ll n, q;
	cin >> n >> q;
	vector<ll> servers(n);
	for(ll i = 0; i < q; i++){
		ll t, k, d;
		cin >> t >> k >> d;
		for(ll s = 0; s < n; s++){
			if(servers[s] < t){
				servers[s] = 0;
			}
		}
		ll zs = count(servers.begin(), servers.end(), 0);
		//cout << "nzs" << nzs << endl;
		if(zs >= k){
			ll countr = k;
			ll used = 0;
			for(ll s = 0; s < n; s++){
				if(countr == 0){
					break;
				}
				if(servers[s] == 0){
					servers[s] = t + d -1;
					used+= s+1;
					countr--;
				}
			}
			cout << used << endl;
		} else {
			cout << -1 << endl;
		}
	}

// 	n, q = [int(x) for x in input().strip().split()]
// asdf = []
// for i in range(q):
//     t, k, d = [int(x) for x in input().strip().split()]
//     asdf.append((t,k,d))
// servers = [0]*n
// for t,k,d in asdf:
//     for ind, i in enumerate(servers):
//         if i < t:
//             servers[ind] = 0
//     if len([x for x in servers if x==0]) >= k:
//         countr = k
//         used=[]
//         for ind, i in enumerate(servers):
//             if countr == 0:
//                 break
//             if i == 0:
//                 servers[ind] = t + d - 1
//                 used.append(ind+1)
//                 countr-=1
//         print(sum(used))
//     else:
//         print(-1)
// #dammit times out in python :((((

}