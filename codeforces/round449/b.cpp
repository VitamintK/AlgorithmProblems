#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll k, p;
	cin >> k >> p;
	ll ans = 0;
	ll count = 0;
	
	ll num = 1;
	ll digits = 1;
	while(count < k){
		if(num >= pow(10, digits)){
			num = pow(10, digits);
			digits++;
		}
		ans += num * pow(10, digits);
		ans %= p;
		ll rev_sum = 0;
		ll t = num;
		while(t){
			rev_sum*= 10;
			rev_sum += t%10;
			t/=10;
		}
		ans += rev_sum;
		ans %= p;
		count++;
		num++;
	}
	cout << ans << endl;
	return 0;
}