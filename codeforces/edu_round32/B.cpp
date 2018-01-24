#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int n, pos, l, r;
	cin >> n >> pos >> l >> r;
	int ans = 0;
	if(l>1 && r < n){
		ans += (r-l);
		ans += min(abs(l - pos), abs(r - pos));
		ans += 2;
	} else if(l>1){
		ans += abs(l - pos) + 1;
	} else if(r < n){
		ans += abs(r-pos) + 1;
	}
	cout << ans << endl;
	return 0;
}