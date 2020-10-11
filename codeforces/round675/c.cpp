#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <utility>
#include <iomanip>
#include <cmath>

#define ll long long
#define ull unsigned long long
using namespace std;

ll MOD = 1000000007;

ll ctoll(char c) {
    ll i = c-'0';
    return i;
}

int main(){
	std::ios::sync_with_stdio(false);
    string s;
    cin >> s;
    ll ans = 0;
    int sumsofar = 0;
    int n = s.length();
    for(ll i = 0; i < n; i++){
        ans *= 10;
        ans%=MOD;
        // i is how many to the left
        ll r = n-i;
        // r is how many to the right
        ll mult = (i*(i+1))/2;
        // cout << s[i] << " gets used in its original spot " << mult << " times" << endl; 
        mult %= MOD;
        ans += (ctoll(s[i])*mult)%MOD;
        ans %= MOD;
        // cout << "sum so far is " << sumsofar << " and r is " << r << endl;
        ans += (sumsofar * r)%MOD;
        sumsofar += ctoll(s[i]);
        // multiply ans by 10 and mod
    }
    cout << ans << endl;
	return 0;
}