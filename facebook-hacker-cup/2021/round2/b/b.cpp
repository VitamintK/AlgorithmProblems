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
vector<int> parent;
vector<vector<int> > children;
vector<int> fs;
map<int, int> fcount;
map<int, map<int,int>> all_counts;

void root(int i){
    for(int u=0; u<edges[i].size();u++){
        if (edges[i][u] == parent[i]){
            continue;
        }
        parent[edges[i][u]] = i;
        children[i].push_back(edges[i][u]);
        root(edges[i][u]);
    }
}

int dfs(int i){
    int ans = 0;
    for(int j=0; j < children[i].size();j++){
        int u = children[i][j];
        ans += dfs(u);
    }
    map<int, int> combined;
    for(int j=0; j < children[i].size();j++){
        int u = children[i][j];
        bool good = true;
        map<int, int> cnt = all_counts[u];
        for(auto it=cnt.begin(); it!=cnt.end();it++){
            if(it->second != 0 && it->second != fcount[it->first]){
                good = false;
                combined[it->first] += it->second;
            }
        }
        if(good){
            ans++;
        }
    }
    combined[fs[i]]++;
    all_counts[i] = combined;
    return ans;
}

int main(){
	std::ios::sync_with_stdio(false);
	int T;
    cin >> T;
    int n;
    for(int t= 0; t<T; t++){
        cin >> n;
        edges.clear();
        edges.resize(n);
        for(int i = 0; i<n-1;i++){
            int u,v;
            cin >> u >> v;
            u--;v--;
            edges[u].push_back(v);
            edges[v].push_back(u);
        }
        fs.resize(n);
        fcount.clear();
        for(int i = 0; i < n;i++){
            cin >> fs[i];
            fcount[fs[i]]+=1;
        }
        parent.resize(n);
        parent.clear();
        children.clear();
        children.resize(n);
        root(0);
        all_counts.clear();
        int ans = dfs(0);
        cout << "Case #" << t+1 << ": " << ans << endl;
    }
	return 0;
}