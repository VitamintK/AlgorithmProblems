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
typedef pair<int, int> pii;
typedef long long ll;

struct Edge{
	int u;
	int v;
	int w;
};

class Compare{
public:
	bool operator() (const Edge &a, const Edge &b){
		return a.w < b.w;
	}
};

int T, N, M, u,v,w, l,h, Q;
vector<Edge> edges;
vector<int> djset;

int find(vector<int> &C, int x) { return (C[x] == x) ? x : C[x] = find(C, C[x]); }
void merge(vector<int> &C, int x, int y) { C[find(C, x)] = find(C, y); }

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> T;
	for (int t = 0; t < T; t++){
		edges.clear();
		cin >> N >> M;
		for (int m = 0; m < M; m++){
			cin >> u >> v >> w;
			u--;v--;
			edges.push_back((Edge){u,v,w});
		}

		sort(edges.begin(), edges.end(), Compare());


		cin >> Q;
		ll cost = 0;
		for (int q = 0; q < Q; q++){
			cin >> l >> h;
			l -= cost;
			h -= cost;
			cost = 0;
			auto it = lower_bound(edges.begin(), edges.end(), (Edge){-1,-1,l}, Compare());
			
			djset.clear();
			djset.resize(N);
			int counter = 0;
			for(int i = 0; i < N; i++) djset[i] = i;
			for(;it != edges.end() && it->w <= h && counter < N-1; it++){
				if (find(djset, it->u) != find(djset, it->v)){
					counter++;
					merge(djset, it->u, it->v);
					cost += it->w;
				}
			}
			cout << cost << '\n';
		}


	}
}