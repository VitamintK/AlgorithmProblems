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
//kevin wang

int main(){
	ll T;
	cin >> T;
	ll n;
	for(ll i = 0; i < T; i++){
		cin >> n;
		ll og_n = n;
		while(n != 1){
			bool fact_found = false;
			for(ll x = 2; x <= n; x++){
				if(n%x == 0){
					fact_found = true;
					double d;
					if(x%2 == 0){
						 d = n/(x+0.5);
					} else {
						 d = n/x;
					}
					if(floor(d) == ceil(d)){
						cout << og_n << " = ";
						cout << x;
						for(ll j = 1; j < d; j++){
							cout << " + " << x+j;
						}
						cout << endl;
					}
				}
			}
		}
	}	
}