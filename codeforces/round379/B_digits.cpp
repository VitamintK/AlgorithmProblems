#include <bits/stdc++.h>

#define ll long long
using namespace std;

int main(){
	//2, 3, 5, 6
	ll a, b, c, d;
	cin >> a >> b >> c >> d;
	ll bigs = 0;
	ll smalls = 0;
	bigs = min({a, c, d});
	a -= bigs;
	c-= bigs;
	d-= bigs;
	smalls = min(a, b);
	cout << smalls*32 + bigs*256 << endl;
}