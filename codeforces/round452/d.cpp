#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n;
	ll ans = 0;
	int digits = 0;
	ll num = 0;
	while(true){
		if(num*10 + 9 > n + n - 1){
			break;
		}
		num = num*10 + 9;
		digits++;
	}
	if(digits == 0){
	 	cout << (n*(n-1))/2 << endl;
	 	return 0;
	}
	ll target;
	for(int i = 0; i < 10; i++){
		target = num + i*(num+1);
		ll middle = target/2;
		if(middle >= n){
			break;
		}
		ans += min(n, target - 1) - middle;
	}

	cout << ans << endl;
	return 0;
}