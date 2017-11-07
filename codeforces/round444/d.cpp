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
		if(i > 0){
			window[xs[i-1]]--;
		}
		//if(fpoint < i){
			//window[xs[i]]++;
			//fpoint = i;
		//}
		ll earliest;
			if(i == 0){
					earliest = 0;
				} else {
					earliest = ts[i-1]+1;
			}
		while(fpoint < n-1 && ts[fpoint+1] < ts[i] + len){
			fpoint++;
			window[xs[fpoint]]++;
					

			if(og + (c-a)*window[1] - (d-b)*window[0] >= 0){
				if(ts[fpoint] - earliest + 1 >= len){
					cout << ts[fpoint] - len + 1  << endl;
					return 0;
				}
			}
		}
		if(og + (c-a)*window[1] - (d-b)*window[0] >= 0){
				cout << earliest << endl;
				cout << "THIS " << endl;
				return 0;
		}
	}
	if(og >= 0){
		cout << ts[n-1] + 1 << endl;
	} else {
		cout << -1 << endl;
	}
	return 0;
}