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
	ll fact[202];
	fact[0] = 1;
	for(ll i = 1; i <= 201; i++){
		fact[i] = fact[i-1]*i;
	}
	ll p;
	cin >> p;
	ll id;
	ll S;
	for(ll i = 0; i < p; i++){
		cin >> id >> S;
		ll ans = 0;
		for(ll twos = 0; twos*2 <= S;twos+=2){
			if((S-twos*2) <= twos){
				ll ones = (S-twos*2);
				ll res = fact[(twos/2)+(ones/2)]/(fact[twos/2]*fact[ones/2]);
				ans += res*res;
			}
		}
		cout << id << " " << ans << endl;
	}
}