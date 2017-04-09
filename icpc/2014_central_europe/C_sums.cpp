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
		bool found = false;
		for(ll d = 2; d < (n+1)/2; d++){
			if ((n-(d*(d-1))/2)%d == 0){
				found = true;
				ll x = (n - (d*(d-1)/2))/d;
				cout << n << " = ";
				cout << x;
				for(ll j = 1; j < d; j++){
					cout << " + " << x+j;
				}
				cout << endl;
				break;
			}
		}
			if (found == false){
				cout << "IMPOSSIBLE" << endl;
			}
		
	}	
}
// 			if((d*d*(d-1))%(2) == 0 && n - (d*d*(d-1))/2 > 0){
// 				found = true;
// 				ll x = n - (d*d*(d-1))/2;
// 				cout << n << " =";
// 				for(ll j = 0; j < d; j++){
// 					cout << " " << x+j;
// 				}
// 				cout << endl;
// 			}
// 		}
// 		if(found == false){
// 			cout << "IMPOSSIBLE" << endl;
// 		}
// 	}
// }