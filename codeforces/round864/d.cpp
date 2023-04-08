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

vector<ll> importances;
vector<vector<int> > edges;
vector<int> parents;
vector<set<pair<ll, int>>> children;
vector<ll> subtree_importance;
vector<ll> subtree_sizes;

int dfs(int v, int parent){
    // return the size of subtree
    int ans = 1;
    ll my_importance = importances[v];
    for(int i=0; i < edges[v].size(); i++){
        int u = edges[v][i];
        if (u==parent){continue;}
        parents[u] = v;
        int subtree_size = dfs(u, v);
        ans += subtree_size;
        children[v].insert(make_pair(-subtree_size, u));
        my_importance += subtree_importance[u];
    }
    subtree_importance[v] = my_importance;
    subtree_sizes[v] = ans;
    return ans;
}

int main(){
	std::ios::sync_with_stdio(false);
	int n, m;
    cin >> n >> m;
    importances.resize(n);
    for(int i = 0; i < n; i++){
        cin >> importances[i];
    }
    edges.resize(n);
    for(int i = 0; i < n-1; i++){
        int u, v; 
        cin >> u >> v;
        edges[u-1].push_back(v-1);
        edges[v-1].push_back(u-1);
    }
    subtree_importance.resize(n);
    subtree_sizes.resize(n);
    children.resize(n);
    parents.resize(n);
    dfs(0, 0);

    for(int i = 0; i < m; i++){
        int t, x;
        cin >> t >> x;
        if (t==1){
            cout << subtree_importance[x-1] << endl;
        } else {
            x--;
            if(children[x].size()==0){
                continue;
            }
            pair<ll, int> heavy_son = *children[x].begin();
            int heavy_son_id = heavy_son.second;
            ll heavy_son_size = -heavy_son.first;
            ll heavy_son_importance = subtree_importance[heavy_son_id];
            ll x_size = subtree_sizes[x];
            int parent = parents[x];
            // calculate new sizes and importances for x and heavy_son
            // heavy_son's importance and size are both set to x's old values
            // x's importance and size simply subtract heavy_son's old values
            subtree_importance[heavy_son_id] = subtree_importance[x];
            subtree_importance[x] -= heavy_son_importance;
            ll new_x_size = x_size - heavy_son_size;
            ll new_heavy_son_size = x_size;
            subtree_sizes[x] = new_x_size;
            subtree_sizes[heavy_son_id] = new_heavy_son_size;
            // set parents
            parents[x] = heavy_son_id;
            parents[heavy_son_id] = parent;
            // set children
            children[parent].erase(make_pair(-x_size, x));
            children[x].erase(heavy_son);
            children[parent].insert(make_pair(-new_heavy_son_size, heavy_son_id));
            children[heavy_son_id].insert(make_pair(-new_x_size, x));
        }
    }
	return 0;
}