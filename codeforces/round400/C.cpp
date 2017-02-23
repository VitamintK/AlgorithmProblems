#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n, k;
	cin >> n >> k;
	map<ll, ll> prefix_sum_counts;
	ll prefix_sum = 0;
	ll ans = 0;
	prefix_sum_counts[0]++;
	for(ll i = 0; i < n; i++){
		ll a;
		cin >> a;
		prefix_sum+=a;
		for(ll p = 0; (pow(k,p) < 10e15) && !(k==1 && p > 0) && !(k==-1 && p > 1); p++){
			ans+=prefix_sum_counts[prefix_sum-pow(k,p)];
		}
		prefix_sum_counts[prefix_sum]++;
	}
	cout << ans << endl;
	return 0;
}