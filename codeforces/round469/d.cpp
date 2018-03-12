#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	int q;
	cin >> n >> q;
	for(int i = 0; i < q; i++){
		ll x;
		cin >> x;
		while(x%2 != 1){
			ll already_in_place = x/2;
			ll not_in_place = n-already_in_place;
			x = x+not_in_place;
		}
		cout << (x+1)/2 << endl;
	}
	return 0;
}