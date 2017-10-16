#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	long n, m, f, s, t;
	cin >> n >> m >> f >> s >> t;
	//id, cost
	vector<vector<pair<long, long> > > roads(n+1);
	vector<vector<pair<long, long> > > air(n+1);
	for(long x = 0; x < m; x++){
		long i, j, c;
		cin >> i >> j >> c;
		roads[i].push_back(make_pair(j, -c));
		roads[j].push_back(make_pair(i, -c));
	}
	for(long x = 0; x < f; x++){
		long u, v;
		cin >> u >> v;
		air[u].push_back(make_pair(v, 0));
	}
	//cost, (id, flight_used)
	priority_queue<pair<long, pair<long, bool>>> pq;
	pq.push(make_pair(0, make_pair(s,0)));
	set<pair<long, bool>> explored;
	while(!pq.empty()){
		pair<long, pair<long, bool> > ex = pq.top();
		long cost = ex.first;
		long id = ex.second.first;
		bool flight_used = ex.second.second;
		pq.pop();
		if(id == t){
			cout << -cost;
			return 0;
		}
		if(explored.count(make_pair(id, flight_used)) > 0){
			continue;
		}
		//cout << id << " " << cost << " " << flight_used << endl;
		explored.insert(make_pair(id, flight_used));

		for(long i = 0; i < roads[id].size(); i++){
			if(explored.count(make_pair(roads[id][i].first, flight_used)) == 0){
				pq.push(make_pair(cost+roads[id][i].second, make_pair(roads[id][i].first, flight_used)));
			}		
		}
		if(flight_used == false){
			for(long i = 0; i < air[id].size(); i++){
				if(explored.count(make_pair(air[id][i].first, true)) == 0){
					pq.push(make_pair(cost, make_pair(air[id][i].first, true)));
				}		
			}
		}

	} 
	return 0;
}