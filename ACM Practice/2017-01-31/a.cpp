#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n, k;
	cin >> n >> k;
	for(ll i = 1; i <= floor(sqrt(n)); i++){
		if(n%i == 0){
			k--;
			if(k == 0){
				cout << i << endl;
				return 0;
			}
		}
	}
	for(ll i = floor(sqrt(n)); i >= 1; i--){
		if(n/i == sqrt(n)){
			continue;
		}
		if(n%i == 0){
			k--;
			if(k == 0){
				cout << n/i << endl;
				return 0;
			}
		}
	}
	cout << -1 << endl;
	
	return 0;
}