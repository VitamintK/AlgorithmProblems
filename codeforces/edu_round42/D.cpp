#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int n;
	cin >> n;
	vector<ll> as(n);
	map<ll, set<ll> > num_map;
	for(int i = 0; i < n; i++){
		cin >> as[i];
		num_map[as[i]].insert(i);
	}
	for(auto const& x: num_map){
		ll num = x.first;
		if(x.second.size() > 1){
			ll prev = -1;
			for(auto const& index: x.second){
				if(prev != -1){
					as[prev] = -1;
					as[index]*=2;
					num_map[as[index]].insert(index);
					prev = -1;
				} else {
					prev = index;
				}
			}
		}
	}
	int k = 0;
	for(int i = 0; i < n; i++){
		if(as[i] != -1){
			k++;
		}
	}
	cout << k << endl;
	for(int i = 0; i < n; i++){
		if(as[i] != -1){
			cout << as[i] << " ";
		}
	}
	return 0;
}