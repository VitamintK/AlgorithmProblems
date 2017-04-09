#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
#include <utility>
#define ll long long
using namespace std;
/*2
3
start 2
end 0
midway 50
3
start midway 1
end midway 90
start end 99
5
start 1
end 0
amity 2
atlantis 3 
azkaban 4
5
start end 101
start amity 1
atlantis amity 2
azkaban atlantis 3
azkaban start 1*/
int main(){
	ll t;
	cin >> t;
	ll n;
	for(ll i = 0; i < t; i++){
		cin >> n;
		string name;
		ll fuel;
		map<string, ll> nodes;
		map<string, vector<pair<ll, string> > > edges;
		for(ll j = 0; j < n; j++){
			cin >> name >> fuel;
			nodes[name] = fuel;
		}
		ll m;
		cin >> m;
		string to;
		for(ll j =0 ; j < m; j++){
			cin >> name >> to >> fuel;
			edges[name].push_back(make_pair(fuel, to));
			edges[to].push_back(make_pair(fuel, name));
		}
		map<string, ll> distances;
		for(auto k : nodes){
			distances[k.second] = 1e20;
		}
		priority_queue<pair<ll, pair<ll, string> > > frontier;
		frontier.push(make_pair(0, make_pair(0, "start")));
		//map<string, map<ll, ll> > shortest_distances;
		set<pair<string,ll> > explored;
		while(!frontier.empty()){
			pair<ll, pair<ll, string>> ex = frontier.top();
			string place = ex.second.second;
			ll fuel_has = ex.second.first;
			ll path_cost = ex.first;
			ll new_fuel_has = nodes[place] + fuel_has;
			frontier.pop();
			if(place == "end"){
				cout << path_cost << endl;
				break;
			}
			if(explored.count(make_pair(place, fuel_has)) < 1){
				explored.insert(make_pair(place, fuel_has));
				for(ll j = 0; j < edges[place].size(); j++){
					if(explored.count(make_pair(edges[place][j].second, new_fuel_has)) < 1){
						frontier.push(make_pair(edges[place][j].first + path_cost,make_pair(edges[place][j].second, new_fuel_has)));
					}
				}
			}
		}
	}
}