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
	std::ios_base::sync_with_stdio (false);
	string og;
	cin >> og;
	string S = og;
	ll m;
	cin >> m;
	ll a, b, c, d;
	for(ll p = 0; p < m; p++){
		cin >> a;
		if(a == 1){
			cin >> b >> c >> d;
            b = b-1;
            c = c-1;
            d = d-1;
			//b is i, c is j, d is k
			bool good = true;
			for(ll i = 0; i < 1+c-b; i++){
				if(S[d+i] != S[b+i]){
					good = false;
					cout << "N" << endl;
					break;
				}
			}
			if(good){
				cout << "Y" << endl;
			}
		}
		if(a ==2){
			cin >> b >> c >>d;
            b = b-1;
            c = c-1;
            d = d-1;
			for(ll i = 0; i < c-b + 1; i++){
				S[b+i] = og[d+i];
			}
		}
		if(a==3){
			cin >> b >> c;
            b = b-1;
            c = c-1;
			for(ll i = b; i <= c; i++){
				if(S[i] == 'z'){
					S[i] = 'a';
				} else {
					S[i] = (char)(S[i]++);
				}
			}
		}
	}
	
}