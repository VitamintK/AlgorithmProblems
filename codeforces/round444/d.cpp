//unfinished.  problem statement was wrong.  i read the wrong problem statement wrong anyways.
#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll n,a,b,c,d,start,len;
	cin >> n >> a >> b >> c >> d >> start >> len;
	vector<ll> ts(n);
	vector<ll> xs(n);
	//ll og = start;
	for(int i = 0; i < n; i++){
		cin >> ts[i] >> xs[i];
		if(xs[i] == 1){
	//		og += a;
		} else {
	//		og -= b;
		}
	}
	vector<ll> window(2);
	int fpoint = -1;
	for(int i = 0; i < n; i++){
		
	}
	if(og >= 0){
		cout << ts[n-1] + 1 << endl;
	} else {
		cout << -1 << endl;
	}
	return 0;
}