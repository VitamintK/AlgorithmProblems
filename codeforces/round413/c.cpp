#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n, c, d;
	cin >> n >> c >> d;
	ll b, p;
	char t;
	vector<pair<ll,ll>> C;
	vector<pair<ll,ll>> D;
	//vector<ll> cs(100001);
	//vector<ll> ds(100001);
	for(ll i = 0; i < n; i++){
		cin >> b >> p >> t;
		if(t == 'C'){
			C.push_back(make_pair(p,b));
			//cs[p] = max(b, cs[p]);
		} else {
			D.push_back(make_pair(p,b));
			//ds[p] = max(b, ds[p]);
		}
	}
	for(ll i = 0; i < n; i++){

	}
	sort(C.begin(), C.end());
	sort(D.begin(), D.end());
	vector<ll> cs;
	vector<ll> ds;
	cs.push_back(0);
	if(C.size() > 0){
	for(ll i = 0; i < C.size()-1; i++){
		cs.push_back(max(cs.back(), C[i].second));
	}
	}
	ds.push_back(0);
	if(D.size() > 0){
		for(ll i = 0; i < D.size()-1; i++){
		ds.push_back(max(ds.back(), D[i].second));
		}
	}
	ll best_d = 0;
	for(ll i = 0; i < D.size(); i++){
		if(D[i].first <= d)
			best_d = max(best_d, D[i].second);
	}

	ll best_c = 0;
	for(ll i = 0; i < C.size(); i++){
		if(C[i].first <= c)
			best_c = max(best_c, C[i].second);
	}
	ll ans = 0;
	if(best_d != 0 && best_c != 0){
		ans = max(ans, best_d + best_c);
	}

	ll cmax = 0;
	ll cpoint = 0;
	if(C.size() > 0){
	for(ll i = C.size() -1; i >= 0; i--){
		while(C[cpoint].first <= c-C[i].first && cpoint < i){
			//cmax = max(cmax, C[cpoint].second);
			//ans = max(ans, cmax + C[i].second);
			cpoint++;
		}
		//cout << C[i].second << " " << cs[cpoint]  << endl;

		if(cs[cpoint] != 0){
			if(cpoint > i){
				cpoint = i;
			}
			ans = max(ans, C[i].second + cs[cpoint]);
		}
		//if(cpoint == i)
		//	break;
	}
}

	ll dmax = 0;
	ll dpoint = 0;
	if(D.size() > 0){
	for(ll i = D.size() -1; i >= 0; i--){
		while(D[dpoint].first <= d-D[i].first && dpoint != i){
			//cmax = max(cmax, C[cpoint].second);
			//cout << C[i].second << " " << cmax << endl;
			//ans = max(ans, cmax + C[i].second);
			dpoint++;
		}
		if(ds[dpoint] != 0){
			if(dpoint > i){
				dpoint = i;
			}
			ans = max(ans, D[i].second + ds[dpoint]);
		}
		//if(dpoint == i)
	//		break;
	}
}
	cout << ans << endl;
	return 0;
}