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
	ll og;
	bool flag = false;
	while(cin >> n){
		if(!flag){ flag = true; } else { cout << endl; }
		og = n;
		ll ans = 0;
		while(n/10 > 0){
			ll a = 1;
			while(n != 0){
				a*= n%10;
				n/=10;
			}
			n = a;
			ans++;
		}
		cout << og << " " << ans;
	}
}