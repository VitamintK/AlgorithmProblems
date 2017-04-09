#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<queue>
#include <utility>
#include <vector>
using namespace std;


int main() {
    //basic idea: BFS (breadth-first search)
    int n;
    cin >> n;
    for(int i = 1; i < n; i++){
        for(int j = 1; j < n; j++){
            queue<pair<int, pair<int, int>>> q;
            vector<vector<int>> g(n, vector<int>(n, -1));
            q.push(make_pair(1,make_pair(0,0)));
            while(!q.empty()){
                pair<int, pair<int, int>> ex = q.front();
                q.pop();
                int exlen = ex.first;
                pair<int, int> exloc = ex.second;
                vector<pair<int,int>> d = {make_pair(i, j), make_pair(i, -j), make_pair(-i, j), make_pair(-i, -j)
                                          ,make_pair(j, i), make_pair(j, -i), make_pair(-j, i), make_pair(-j, -i)};
                for(int k = 0; k < d.size(); k++){
                    int newrow = exloc.first + d[k].first;
                    int newcol = exloc.second + d[k].second;
                    if(newrow >= 0 && newrow < n && newcol >= 0 && newcol < n && g[newrow][newcol] == -1){
                        g[newrow][newcol] = exlen;
                        q.push(make_pair(exlen+1, make_pair(newrow, newcol)));
                    }
                }
            }
            cout << g[n-1][n-1] << " ";
            
        } cout << endl;

    }
    return 0;
}