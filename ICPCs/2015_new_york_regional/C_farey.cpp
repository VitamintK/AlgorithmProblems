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
ll tsm[10001];
ll ts(ll n){
	//this returns the count of a,b pairs where 1<=a<b<=n where gcd(a,b) = 1 (aka a and b are coprime)
	//kernel of code from here http://codegolf.stackexchange.com/questions/26739/super-speedy-totient-function
	//the big leap is that the number of a,b pairs where 1<=a<b<=n where gcd(a,b) = i is ts(n/i)
	if(tsm[n] != -1){
		return tsm[n]; //check cache
	}
	//to find the number of a,b pairs where gcd(a,b) =1, we first find
	ll ans = (n * (n-1))/2; //all possible a,b pairs where a<=a<b<=n
	for(ll i = 2; i <= n; i++){ 
		ans-=ts(n/i); //minus the a,b pairs where gcd(a,b) = i for all i from 2 to n
	}
	tsm[n] = ans; //memoize
	return ans;
}

int main(){
	for(ll i = 0; i < 10001; i++){
		tsm[i] = -1;
	}
	tsm[0] = 0;
	tsm[1] = 0;
	ll n;
	ll id;
	ll q;
	cin >> q;
	for(ll i = 0; i < q; i++){
		cin >> id >> n;
		cout << id << " " << ts(n)+2 << endl; //+1 for 0/1 and 1/1
		    //(not included in ts(n) because 1/1 does not fulfill a<b and 0/1 does not fulfill 1<=a)
	}
}