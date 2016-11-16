#include <bits/stdc++.h>
#include <cmath>

#define REP(i,a,b) for(int i = (a); i < b; i++)
#define ll long long
using namespace std;
int main(){
	ll n;
	vector<ll> phi(1000003);
	vector<ll> ans(1000003);
	vector<ll> primes(1000002, 0);
	for(ll i = 2; i < 1000001;i++){
		if(primes[i] == 0){
			for(ll j = i; j < 1000001; j+=i){
				if(primes[j] == 0){
					primes[j] = i;
				}
			}
		}
	}
	phi[1] = 1;
	ans[1] = 1;
	for(ll i = 2; i < 1000001; i++){
		map<ll, ll> factors;
		ll a = i;
		while(a != 1){
			if(primes[a] != 0){
				factors[primes[a]]++;
			} else {
				break;
			}
			a/=primes[a];
			//cout << a << endl;
			//cout << primes[a] << endl;
		}
		ll facs = 1;
		for(auto asdf : factors){
			facs *= pow(asdf.first, asdf.second -1) * (asdf.first - 1);
		}
		phi[i] = facs;
		ans[i] = ans[i-1] + phi[i];
	}
	while(cin >> n){
		cout << 2 + ans[n] * 2 << endl;
	}
}

