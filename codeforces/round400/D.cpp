#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	
	ll n, m;
	cin >> n >> m;
	vector<ll> doors(n);
	vector<vector<ll>> doorfriends(n);
	vector<ll> switches(m, -1);
	vector<vector<ll>> switchfriends(m);
	set<ll> doors_not_allocated;

	for(ll i =0 ; i < n; i++){
		cin >> doors[i];
		doors_not_allocated.insert(i);
	}
	for(ll i = 0; i < m; i++){
		ll x;
		cin >> x;
		for(ll j = 0; j < x; j++){
			ll d;
			cin >> d;
			doorfriends[d-1].push_back(i);
			switchfriends[i].push_back(d-1);
		}
	}
	vector<ll> dq;
	vector<ll> sq;
	while(!doors_not_allocated.empty()){
		ll door = *doors_not_allocated.begin();
		doors_not_allocated.erase(door);
		if(doors[door] == 1){
			switches[doorfriends[door][0]] = 0;
			switches[doorfriends[door][1]] = 0;
		} else {
			switches[doorfriends[door][0]] = 0;
			switches[doorfriends[door][1]] = 1;
		}
				for(ll i = 0; i <= 1; i++){
					for(ll j = 0; j < switchfriends[doorfriends[door][i]].size(); j++){
						if(switchfriends[doorfriends[door][i]][j] != door &&
							doors_not_allocated.count(switchfriends[doorfriends[door][i]][j]) > 0){
							dq.push_back(switchfriends[doorfriends[door][i]][j]);
							doors_not_allocated.erase(switchfriends[doorfriends[door][i]][j]);
						}
					}
				}
		while(!dq.empty()){
			door = dq.back();
			dq.pop_back();
			//doors_not_allocated.erase(door);
			ll switch_we_care_about;
			if(switches[doorfriends[door][0]] > -1 && switches[doorfriends[door][1]] > -1){
				continue;
			} else if(switches[doorfriends[door][0]] > -1){
				switches[doorfriends[door][1]] = doors[door]^1^switches[doorfriends[door][0]];
				switch_we_care_about = 1;
			} else {
				switches[doorfriends[door][0]] = doors[door]^1^switches[doorfriends[door][1]];
				switch_we_care_about = 0;
			}
			//
				//for(ll i = 0; i <= 1; i++){
				ll i = switch_we_care_about;
					for(ll j = 0; j < switchfriends[doorfriends[door][i]].size(); j++){
						if(switchfriends[doorfriends[door][i]][j] != door &&
							doors_not_allocated.count(switchfriends[doorfriends[door][i]][j]) > 0){
							dq.push_back(switchfriends[doorfriends[door][i]][j]);
							doors_not_allocated.erase(switchfriends[doorfriends[door][i]][j]);
						}
					}
				//}
		}
	}
	for(ll i = 0; i < n; i++){
		if(doors[i] ^ switches[doorfriends[i][0]] ^ switches[doorfriends[i][1]] == 0){
			//cout << i << " " << doors[i] << " " << switches[doorfriends[i][0]] << " " << switches[doorfriends[i][1]] << endl;
			cout <<"NO" << endl;
			return 0;
		}
	}
	cout << "YES" << endl;
	//number of doors that switch a controls could be 0
	return 0;
}