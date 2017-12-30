#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll n, a, b;
	cin >> n >> a >> b;
	for(ll i = 0; i < 100000005; i++){
		if(a*i > n){
			break;
		}
		if(((n - a*i)%b) == 0){
			cout << "YES" << endl;
			cout << i << " " << ((n - a*i)/b) << endl;
			return 0;
		}
	}
	cout << "NO" << endl;
	return 0;
}