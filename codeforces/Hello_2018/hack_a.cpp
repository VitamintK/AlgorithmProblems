#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	// ll a, b, m;
	// cin >> b >> a;
	// m = pow(2,b);
	// cout << m << endl;
	// ll ans = a%m;
	// cout << ans << endl;
	int a, b;
	cin >> a >> b;
	int c = pow(2,a);
	if(b%c == 0){
		cout << "0";
	} else {
		cout << b%c;
	}
	return 0;
}