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
	long long n, m, k;
	long long colors[200001];
	cin >> n >> m >> k;
	vector<vector<long long> > edges(n);
	set<long long> to_explore;
	for(long long i = 0; i < n; i++){
		cin >> colors[i];
		to_explore.insert(i);
	}
	long long l, r;
	for(long long i = 0; i < m; i++){
		cin >> l >> r;
		edges[l-1].push_back(r-1);
		edges[r-1].push_back(l-1);
	}
	long long ans = 0;
	while(!to_explore.empty()){
		long long root = *to_explore.begin();
		vector<long long> stack;
		long long maxcol = 0;
		long long socknum = 0;
		map<long long, long long>colcount;
		stack.push_back(root);
		while(!stack.empty()){
			long long explorino = stack.back();
			stack.pop_back();
			if(to_explore.count(explorino) > 0){
				to_explore.erase(explorino);
				socknum++;
				colcount[colors[explorino]]++;
			}
			maxcol = max(maxcol, colcount[colors[explorino]]);
			for(long long neighj = 0; neighj < edges[explorino].size(); neighj++){
				if(to_explore.count(edges[explorino][neighj]) > 0){
					stack.push_back(edges[explorino][neighj]);
				}
			}
		}
		ans+=(socknum - maxcol);
	}
	cout << ans << endl;
}