#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	vector<bool> sieve(100009, false); //sieve where true = composite, false = prime
	for(ll i = 2; i < 100009; i++){
		if(!sieve[i]){
			for(ll j = 2*i; j < 100009; j+=i){
				sieve[j] = true;
			}
		}

	}

	ll n;
	cin >> n;
	if(n <= 2){
		cout << 1 << endl;
	} else {
		cout << 2 << endl;
	}
	for(ll i = 0; i < n; i++){
		if(sieve[i+2] == true){
			cout << 2 << " ";
		} else{
			cout << 1 << " ";
		}
	} cout << endl;
	return 0;
}