#include <bits/stdc++.h>

#define ll long long
using namespace std;

int main(){
	ll n;
	ll xk, yk;
	cin >> n >> xk >> yk;
	vector<pair<ll,char>> u;
	vector<pair<ll,char>> ur;
	vector<pair<ll,char>> r;
	vector<pair<ll,char>> dr;
	vector<pair<ll,char>> d;
	vector<pair<ll,char>> dl;
	vector<pair<ll,char>> l;
	vector<pair<ll,char>> ul;
	for(ll i = 0; i < n; i++){
		ll x, y;
		char t;
		cin >> t >> x >> y;
		if(x-xk == y-yk){
			if(x > xk){
				ur.push_back(make_pair(x-xk,t));
			} else {
				dl.push_back(make_pair(xk-x,t));
			}
		} else if(x == xk){
			if(y > yk){
				u.push_back(make_pair(y-yk,t));
			} else {
				d.push_back(make_pair(yk-y,t));
			}
		} else if(y == yk){
			if(x > xk){
				r.push_back(make_pair(x-xk,t));
			} else {
				l.push_back(make_pair(xk-x,t));
			}
		} else if(xk-x == y-yk){
			if(x > xk){
				dr.push_back(make_pair(x-xk,t));
			} else {
				ul.push_back(make_pair(xk-x,t));
			}
		}
	}
	//cout <<"HI" << endl;
	sort(u.begin(), u.end());
	sort(ur.begin(), ur.end());
	sort(r.begin(), r.end());
	sort(dr.begin(), dr.end());
	sort(d.begin(), d.end());
	sort(dl.begin(), dl.end());
	sort(l.begin(), l.end());
	sort(ul.begin(), ul.end());
	//cout <<"HEY" << endl;
	if(u.size() > 0 && (u[0].second == 'R' || u[0].second == 'Q')){
		cout << "YES" << endl;
		return 0;
	}
	//cout <<"HILSDF" << endl;
	if(ur.size() > 0 && (ur[0].second == 'B' || ur[0].second == 'Q')){
		cout << "YES" << endl;
		return 0;
	}
	if(r.size() > 0 && (r[0].second == 'R' || r[0].second == 'Q')){
		cout << "YES" << endl;
		return 0;
	}
	//cout <<"HI" << endl;
	if(dr.size() > 0 && (dr[0].second == 'B' || dr[0].second == 'Q')){
		cout << "YES" << endl;
		return 0;
	}
	if(d.size() > 0 && (d[0].second == 'R' || d[0].second == 'Q')){
		cout << "YES" << endl;
		return 0;
	}
	if(dl.size() > 0 && (dl[0].second == 'B' || dl[0].second == 'Q')){
		cout << "YES" << endl;
		return 0;
	}
	if(l.size() > 0 && (l[0].second == 'R' || l[0].second == 'Q')){
		cout << "YES" << endl;
		return 0;
	}
	if(ul.size() > 0 && (ul[0].second == 'B' || ul[0].second == 'Q')){
		cout << "YES" << endl;
		return 0;
	}
	cout <<"NO" << endl;
}