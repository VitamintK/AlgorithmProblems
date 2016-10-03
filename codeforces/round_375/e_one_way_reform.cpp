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


int main(){
	int t;
	cin >> t;
	for(int tt = 0; tt < t; tt++){
	int n, m;
	cin >> n >> m;
	int roads[200] = {0};
	int adj[200][200] = {0}; //1 = i goes to j.  -1 = j goes to i
	vector<int> vs[200];
	int ins[200] = {0};
	int outs[200] = {0};
	int u, v;
	for(int i =0; i < m; i++){
		cin >> u >> v;
		roads[u-1]++;
		roads[v-1]++;
		adj[u-1][v-1] = 2;
		adj[v-1][u-1] = 2;
		vs[v-1].push_back(u-1);
		vs[u-1].push_back(v-1);
	}
	int sum = 0;
	for(int i = 0; i < n; i++){
		if(roads[i]%2 == 0){
			sum++;
			for(int j = 0; j < roads[i]; j++){
				int out = vs[i][j];
				if(adj[i][out] == 2){
					if(roads[out]%2 == 0){
						//OUT IS EVEN.
						if(outs[out] >= roads[out]/2){
							adj[i][out] = 1;
							adj[out][i] = -1;
							outs[i]++;
							ins[out]++;
						} else {
							adj[i][out] = -1;
							adj[out][i] = 1;
							outs[out]++;
							ins[i]++;
						}
					} else {
						//OUT IS ODD.
						if(ins[i] < roads[i]/2){
							adj[i][out] = -1;
							adj[out][i] = 1;
							ins[i]++;
							outs[out]++;
						} else {
							adj[i][out] = 1;
							adj[out][i] = -1;
							outs[i]++;
							ins[out]++;
						}
					}
				}
			}
		}
	}
	for(int i = 0; i < n; i++){
		if(roads[i]%2 != 0){
			for(int out = 0; out < n; out++){
				if(adj[i][out] == 2){
					adj[i][out] = -1;
					adj[out][i] = 1;
					ins[i]++;
					outs[out]++;
				}
			}
		}
	}
	cout << sum << endl;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			if(adj[i][j] ==1){
				cout << i+1 << " " << j+1 << endl;
			}
		}
	}
	}
}