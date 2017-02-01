#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n, l, r;
	cin >> n >> l >> r;
	vector<ll> a(n);
	vector<ll> c(n);
	for(ll i = 0; i < n; i++){
		cin >> a[i];
	}
	vector<ll> pos(n);
	for(ll i =0 ; i < n; i++){
		cin >> c[i];
		pos[c[i]-1] = i;
	}
	//for(ll i = 0; i < n; i++){
//		cout << pos[i] << " ";
//	} cout << endl;
	vector<ll> b(n);
	ll maxi = 100000000000;
	ll mini = -100000000000;
	for(ll i =n-1; i >=0; i--){
		//if(maxi + a[c[i]] < l){
		//	cout << -1 << endl;
		//	return 0;
		//}
		if(maxi + a[pos[i]] <= r && maxi + a[pos[i]] >= l){
			b[pos[i]] = maxi + a[pos[i]];
			maxi--;
		} else if(maxi + a[pos[i]] < l){
			cout << -1 << endl;
			return 0;
		}else{
			b[pos[i]] = r;
			maxi = r - a[pos[i]] - 1;
		}
	}
	for(ll i = 0; i < n; i++){
		cout << b[i] << " ";
	} cout << endl;
	return 0;
}