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

map<ll, ll> fibmem;

ll fib(ll k){
	//fast fibonnaci from https://www.nayuki.io/page/fast-fibonacci-algorithms
	if(fibmem.count(k) > 0){
		return fibmem[k];
	}
	if(k == 0){
		return 0;
	}
	if(k == 1 || k == 2){
		return 1;
	}
	if((k&1ll) == 0){

		return (fibmem[k] = (fib(k/2) * (2*fib(k/2 + 1) - fib(k/2)))%1000000000ll);
	}
	else{
		ll s = (fib((k-1)/2+1));
		ll t = fib((k-1)/2);
		return (fibmem[k] = ((s*s) + (t*t))%1000000000ll);
	}
}

int main(){
	ll p;
	cin >> p;
	ll id;
	ll n;
	for(ll i = 0; i < p; i++){
		cin >> id >> n;
		cout << id << " " << (fib(n)+1000000000)%1000000000 << endl;
	}
}