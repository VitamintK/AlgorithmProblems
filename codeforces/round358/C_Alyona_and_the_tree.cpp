#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <utility>
#include <map>
#include <set>
using namespace std;
#typedef ll long long
int main(){
	long long n;
	cin >> n;
	long long node_values[100002] = {0};
	//ll edge_value_to_parent[100002] = {0};
	vector<pair<ll, ll> > children[100001];
	for(long long i = 1; i <= n; i++){
		cin >> node_values[i];
	}
	ll a, b;
	for(ll i = 2; i <= n; i++){
		cin >> a >> b;
		children[a].push_back(make_pair(i, b));
		
	}
	vector<pair<ll, ll> > exploring; //first is node to explore, second is cost so far
	while(!exploring.empty()){
		ll explore = exploring.back();
		exploring.pop_back();
		for(ll child : children[explore.first()]){
			if(child.
		}
	}
	return 0;
}
