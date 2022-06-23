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

vector<int> ps;
vector<vector<int> > children;
vector<ll> rs;
vector<ll> ls;
vector<int> ansv;

int dfs(int v) {
    ll cumflow = 0;
    int ans = 0;
    for(int i=0; i < children[v].size(); i++){
        int flow = dfs(children[v][i]);
        cumflow += flow;
        ans += ansv[children[v][i]];
    }
    if (cumflow < ls[v]){
        ans++;
        cumflow = rs[v];
    }
    ansv[v] = ans;
    // cout << "ansv " << v << " is " << ans << endl;
    return min(cumflow, rs[v]);
}

int main(){
	std::ios::sync_with_stdio(false);
	int T;
    cin >> T;
    for(int t = 0; t < T; t++){
        int n;
        cin >> n;
        ps.resize(n);
        children.resize(n);
        children.clear();
        for (int i=1; i < n; i++){
            cin >> ps[i];
            ps[i]--;
            children[ps[i]].push_back(i);
        }
        ls.resize(n);
        rs.resize(n);
        for(int i =0; i < n; i++){
            cin >> ls[i] >> rs[i];
        }
        ansv.resize(n);
        ansv.clear();
        dfs(0);
        cout << ansv[0] << endl;
    }
    
	return 0;
}