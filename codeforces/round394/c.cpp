#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n, m;
	cin >> n >> m;
	vector<string> ss(n);
	vector<ll> letter(n, m*m*5);
	vector<ll> digit(n, m*m*5);
	vector<ll> special(n, m*m*5);
	for(ll i = 0; i < n; i++){
		cin >> ss[i];
		for(ll j = 0; j < m; j++){
			if(ss[i][j] >= 'a' && ss[i][j] <= 'z'){
				letter[i] = min(letter[i], min(j, m-j));
			}
			if(ss[i][j] >= '0' && ss[i][j] <= '9'){
				digit[i] = min(digit[i], min(j, m-j));
			}
			if(ss[i][j] == '*' || ss[i][j] == '#' || ss[i][j] == '&'){
				special[i] = min(special[i], min(j, m-j));
			}
		}
	}
	// for(ll i = 0; i < n; i++){
	// 	cout << letter[i] << " ";
	// } cout << endl;
	// for(ll i = 0; i < n; i++){
	// 	cout << digit[i] << " ";
	// } cout << endl;
	// for(ll i = 0; i < n; i++){
	// 	cout << special[i] << " ";
	// } cout << endl;
	ll ans = m*m*5;
	for(ll i = 0; i < n; i++){
		for(ll j = 0; j < n; j++){
			for(ll k = 0; k < n; k++){
				if(k == j) continue;
				if(k == i) continue;
				if(i == j) continue;
				ans = min(ans, letter[i] + digit[j] + special[k]);
			}
		}
	}
	cout << ans << endl;
	return 0;
}