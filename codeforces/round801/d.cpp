// g++ -std=c++17 x.cpp && ./a.out
#include <iostream> 
#include <string> 
#include <set> 
#include <map> 
#include <stack> 
#include <queue> 
#include <vector> 
#include <utility> 
#include <iomanip> 
#include <sstream> 
#include <bitset> 
#include <cstdlib> 
#include <iterator> 
#include <algorithm> 
#include <cmath>

#define ll long long
#define ull unsigned long long
using namespace std;

vector<vector<int> > edges;

int dfs(int v, int parent){
    int zeroes = 0;
    int ans = 0;
    for(int i = 0; i < edges[v].size(); i++) {
        if (edges[v][i] == parent) { continue; }
        int needed = dfs(edges[v][i], v);
        if (needed == 0) {
            zeroes++;
        }
        ans += needed;
    }
    if (zeroes > 1) {
        ans += zeroes-1;
    }
    // cout << " I AM " << v << ". score: " << ans << endl;
    return ans;
}

int main(){
	std::ios::sync_with_stdio(false);
	int T;
	cin >> T;
    for(int t=0; t < T; t++){
        int n;
        cin >> n;
        // vector<vector<int> > edges(n, vector<int>(0));
        edges.resize(n);
        edges.clear();
        int highest_degree = -1;
        int high_degree_node = -1;
        for(int i =0; i <n-1; i++){
            int x,y;
            cin >> x >> y;
            x--; y--;
            edges[x].push_back(y);
            edges[y].push_back(x);
            // cout << edges[x].size() << " " << edges[y].size() << endl;
            // cout << x << y << endl;
            if ((int)edges[x].size() > highest_degree) {
                highest_degree = edges[x].size();
                high_degree_node = x;
            }
            if ((int)edges[y].size() > highest_degree) {
                highest_degree = edges[y].size();
                high_degree_node = y;
            }
        }
        // cout << highest_degree << endl;
        // cout << high_degree_node << endl;
        int ans = dfs(high_degree_node, -1);
        if (ans == 0) {
            if (n == 1) {
                cout << 0 << endl;
            } else {
                cout << 1 << endl;
            }
        } else {
            cout << ans << endl;
        }
    }
    
	return 0;
}