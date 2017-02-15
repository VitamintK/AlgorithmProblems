#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n;
	string b;
	cin >> b;
	for(ll i = 0; i < n; i++){
		string a;
		cin >> a;
	}
	if(n%2 == 0){
		cout <<"home" << endl;
	} else {
		cout <<"contest" << endl;
	}
	// cin >> n;
	// string home;
	// cin >> home;
	// map<string, bool> as;
	// string ans;
	// for(ll i = 0; i < n; i++){
	// 	string a;
	// 	cin >> a;
	// 	if(home == a.substr(0,3)){
	// 		as[a.substr(5,3)] = !as[a.substr(5,3)];
	// 	} else {
	// 		as[a.substr(0,3)] = !as[a.substr(0,3)];
	// 	}
	// }
	// for(auto i: as){
	// 	if(i.second == true){
	// 		cout << 'contest' << endl;
	// 		return 0;
	// 	}
	// }
	// cout << "home" << endl;
	return 0;
}