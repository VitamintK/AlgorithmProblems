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
	ll k, m;
	string a;
	for(ll i =0; i < p; i++){
		cin >> k >> m >> a;
		//bleh dont wanna do this in cpp
		//this is a graveyard of the code i was going to write before i realized i'd have to write
		//addition by myself
		for(int iteration = 0; iteration < m; iteration++){
			string b = a;
			for(int pos = 0; pos < a.length(); str++){
				b[pos] = a[a.length()-1-pos];
			}
			
		}
	}
}