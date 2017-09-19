#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>

#define ll long long
#define ull unsigned long long
using namespace std;

map<int,int> primefactor(int a){
	//cout << a << endl;
	int aa = a;
	map<int, int> primes;
	for(int i = 2; i <= sqrt(a); i++){
		while(aa%i == 0){
			primes[i]++;
			//cout << " " << i << endl;
			aa/=i;
		}
	}
	if(aa != 1){
		primes[aa]++;
	}
	return primes;
}

int is_ok(int a, int b){
	//cout << a << " " << b << endl;
	map<int, int> primesa = primefactor(a);
	map<int, int> primesb = primefactor(b);
	for(auto it = primesa.begin(); it != primesa.end(); it++){
		int acount = it->second;
		int bcount = primesb[it->first];
		int mx = max(acount, bcount);
		int mn = min(acount, bcount);
		if((abs(2*mx - mn)%3 != 0) || (mn - (2*mx - mn)/3 < 0)){
			return 0;
		}
	}
	for(auto it = primesb.begin(); it != primesb.end(); it++){
		int acount = it->second;
		int bcount = primesa[it->first];
		int mx = max(acount, bcount);
		int mn = min(acount, bcount);
		if((abs(2*mx - mn)%3 != 0) || (mn - (2*mx - mn)/3 < 0)){
			return 0;
		}
	}
	return 1;
}

int main(){
	std::ios::sync_with_stdio(false);
	int n;
	cin >> n;
	int a, b;
	for(int i =0; i < n; i++){
		cin >> a >> b;
		if(is_ok(a, b)){
			cout << "Yes" << endl;
		} else {
			cout << "No" << endl;
		}
	}
	return 0;
}