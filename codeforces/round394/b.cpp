#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n, l;
	cin >> n >> l;
	vector<ll> a(n);
	vector<ll> b(n);
	for(ll i = 0; i < n; i++){
		cin >> a[i];
	}
	for(ll i = 0; i < n; i++){
		cin >> b[i];
	}
	//for(ll i = n; i > 0; i--){
	//a[n] = a[n] - a[n-1];
	//}
	//for(ll i = n; i > 0; i--){
	//	b[n] = b[n] - b[n-1];
	//}
	for(ll i = 0; i < l; i++){
		for(ll j = n-1; j >=0; j--){
			b[j]--;
			if(b[j] < 0){
				//b.push_back((l + b[j])%l);
				//cout << b[b.size() - 1] << endl;
				//b.erase(b.begin() + j);
				b.erase(b.begin());
				b.push_back(l-1);
			}
		}
		if(equal(a.begin(), a.end(), b.begin())){
			cout << "YES" << endl;
			return 0;
		}
		//for(ll x = 0; x < n; x++){
		//	cout << b[x] << " " ;
		//} cout << endl;
	}
	cout << "NO" << endl;
	return 0;
}