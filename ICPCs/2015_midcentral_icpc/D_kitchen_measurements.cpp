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

using namespace std;

int hahs(vector<int> k){
	int j = 0;
	for(int i = 0; i < k.size()-1; i++){
		j |= k[i];
		j = j << 6;
	}
	j|= k[k.size()-1];
	// cout << "HASHING: " << j << endl;
	return j;
}

int main(){
	set<int> been;
	priority_queue<pair<int, vector<int> > > frontier;
	int capac[5] = {0};
	int n;
	int v;
	cin >> n;
	vector<int> volum (n, 0);
	for(int i = 0; i < n; i++){
		cin >> capac[i];
	}
	cin >> v;
	volum[0] = capac[0];
	frontier.push(make_pair(0, volum));
	while(!frontier.empty()){
		pair<int, vector<int> > explorex = frontier.top();
		frontier.pop();
		vector<int> explore = explorex.second;
		// for(int j = 0; j < explore.size(); j++){
		// 	cout << explore[j] << " ";
		// } cout << endl;
		explorex.first = explorex.first * -1;
		if(been.count(hahs(explore)) > 0){
			//cout << " continue" << endl;
			continue;
		}
		if(explore[0] == v){
			cout << explorex.first << endl;
			return 0;
		}
		been.insert(hahs(explore));
		//make the list of all the edges going out
		for(int pourer = 0; pourer < n; pourer++){
			for(int taker = 0; taker < n; taker++){
				if(explore[pourer] > 0 && explore[taker] < capac[taker] && pourer != taker){
					//ADD AN EDGE TO A NEW STATE TO THE THING.
					int edge_cost;
					vector<int> topush = explore;
					if(topush[pourer] + topush[taker] > capac[taker]){
						//pour until taker is full
						edge_cost = capac[taker] - topush[taker];
						topush[pourer] -= edge_cost;
						topush[taker] = capac[taker];
					} else {
						//pour all
						edge_cost = topush[pourer];
						topush[taker] += topush[pourer];
						topush[pourer] = 0;
					}
					// cout << "pushing: " << endl;
					// cout << " ";
					// for(int j = 0; j < topush.size(); j++){
					// 	cout << topush[j] << " ";
					// } cout << endl;
					frontier.push(make_pair(-1 * (explorex.first + edge_cost), topush));
				}
			}
		}
	}
	cout << "impossible" << endl;
}