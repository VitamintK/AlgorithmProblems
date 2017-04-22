#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

auto compareFunc = [](pair<pair<double, int>,pair<int,int>> a,
 pair<pair<double, int>,pair<int,int>> b) { return a > b; };


int main(){
	std::ios::sync_with_stdio(false);
	int T;
	cin >> T;
	cout << fixed;
	for(int t = 0; t < T; t++){
		int n, Q;
		cin >> n >> Q;
		vector<int> speeds(n);
		vector<int> endurances(n);
		vector<vector<pair<int,int>>> edges(n);
		for(int i = 0; i < n; i++){
			cin >> endurances[i] >> speeds[i];
		}
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				int d;
				cin >> d;
				if(d > -1){
					edges[i].push_back(make_pair(d,j));
				}
			}
		}
		cout << "Case #" << t+1 << ": ";
		for(int q = 0; q < Q; q++){
			//dijkstra
			//total time, endurance left on this horse; node_id, horse_id
			int u, v;
			cin >> u >> v;
			u--; v--;
			priority_queue<pair<pair<double,int>,pair<int,int> >,
			vector<pair<pair<double,int>,pair<int,int> >>, decltype(compareFunc) > pq(compareFunc);
			vector<vector<pair<double,int> > > dp(n, vector<pair<double,int>>(n, make_pair(-1.0,-1)));

			pq.push(make_pair(make_pair(0,endurances[u]), make_pair(u,u)));
			while(!pq.empty()){
				//cout <<"printing queue" << endl;
				//for
				pair<pair<double,int>,pair<int,int>> ppiipii = pq.top();
				pq.pop();
				//cout << "popped " << ppiipii.first.first << ", top now is " << pq.top().first.first << endl;
				//cout << (pq.top() < ppiipii) << endl;
				int from = ppiipii.second.first;
				int horse = ppiipii.second.second;
				double time_so_far = ppiipii.first.first;
				int endurance_left = ppiipii.first.second;
				if(from == v){
					cout <<" " << time_so_far; //<<" lalalalala";

					break;
				}
				if(dp[ppiipii.second.first][ppiipii.second.second].first > -1){
					continue;
				}
				dp[from][horse] = ppiipii.first;
				for(int i = 0; i < edges[ppiipii.second.first].size(); i++){
					int to = edges[ppiipii.second.first][i].second;
					double w = edges[ppiipii.second.first][i].first;
					if(dp[to][from].first < 0 && endurances[from] >= w){
						//cout << w/speeds[from] << endl;
						pq.push(make_pair(make_pair(time_so_far+(w/speeds[from]),endurances[from]-w),make_pair(to,from)));
					}
					if(dp[to][horse].first < 0 && endurance_left >= w){
						pq.push(make_pair(make_pair(time_so_far+(w/speeds[horse]),endurance_left-w),make_pair(to,horse)));
					}
				}
			}
		}
		cout << endl;
	}
	return 0;
}