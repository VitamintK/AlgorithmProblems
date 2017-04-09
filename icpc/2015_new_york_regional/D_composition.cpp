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
	ll n, m, k;
	ll id;
	for(ll i = 0; i < p; i++){
		cin >> id >> n >> m >> k;
		ll dp[32] = {0};
		dp[0] = 1;
		for(ll j = 1; j <= n; j++){
			for(ll subtract = 1; subtract <= j; subtract++){
				if((subtract-m)%k != 0){
					dp[j]+=dp[j-subtract];
				}
			}
		}
		cout << id << " " << dp[n] << endl;
	}
}