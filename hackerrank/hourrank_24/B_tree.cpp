#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;
#define ll long long
vector<vector<int>> edges;
double ans = 0;
double N = 0;

int dfs(ll i,ll p, ll h){
    ll size_of_tree = 1;
    for(ll j = 0; j < edges[i].size(); j++){
        if(edges[i][j] != p){
            size_of_tree += dfs(edges[i][j], i, h+1);
        }
    }
    N += h;
    ans += h * size_of_tree;
    //cout << h << " " << size_of_tree << endl;
    return size_of_tree;
}



int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    ll n;
    cin >> n;
    edges.resize(n);
    for(int i = 0; i < n-1; i++){
        int x,y;
        cin >> x >> y;
        edges[x-1].push_back(y-1);
        edges[y-1].push_back(x-1);
    }
    dfs(0, 0, 0);
    cout << setprecision(10) << n - ans/N << endl;
    return 0;
}
