#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <utility>
#include <iomanip>
#include <functional>

#define ll long long
#define ull unsigned long long
using namespace std;

ll MOD = 1000000007;

vector<int> centroid(const vector<vector<int>> &edges, int n) {
    vector<int> centroid;
    function<int (int, int)> dfs = [&](int u, int prev) {
        int tot = 0;
        int is_centroid = true;
        for(int i = 0; i < edges[u].size(); i ++ ){
            if (edges[u][i] == prev) {
                continue;
            }
            int s= dfs(edges[u][i], u);
            if (s > n/2) {
                is_centroid = false;
            }
            tot += s;
        }
        int up = n - tot - 1;
        if (up > n/2) {
            is_centroid = false;
        }
        if (is_centroid == true) {
            centroid.push_back(u);
        }
        return tot + 1;
    };
    dfs(0, 0);
    return centroid;
}

int find_leaf(const vector<vector<int>> &edges, int start, int parent) {
    int u = start;
    while (edges[u].size() > 1) {
        if (edges[u][0] == parent) {
            parent = u;
            u = edges[u][1];
        } else {
            parent = u;
            u = edges[u][0];
        }
    }
    return u;
}

int main(){
	std::ios::sync_with_stdio(false);
	int T;
    cin >>T;
    for(int t = 0; t < T; t++){
        int n = 0;
        cin >> n;
        vector<vector<int> > edges(n);
        int x, y;
        for(int i = 0; i < n-1; i++){
            cin >> x >> y;
            edges[x-1].push_back(y-1);
            edges[y-1].push_back(x-1);
        }
        vector<int> c = centroid(edges, n);
        // for(int i = 0; i < c.size(); i++){
        //     cout << c[i] << " ";
        // }
        // cout << endl;
        if (c.size() == 1) {
            cout << edges[0][0]+1 << " " << 1 << endl;
            cout << edges[0][0]+1 << " " << 1 << endl;
            continue;
        }
        int f = find_leaf(edges, c[0], c[1]);
        cout << edges[f][0]+1 << " " << f+1 << endl;
        cout << f+1 << " " << c[1]+1 << endl;
    }
	return 0;
}