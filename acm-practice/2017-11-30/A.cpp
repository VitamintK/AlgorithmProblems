#include<bits/stdc++.h>

using namespace std;

int n, m;
vector<vector<int> > grid;
int ans = 0;

void dfs(int r, int c){
    vector<int> dr = {-1, 0, 1, 0};
    vector<int> dc = {0, 1, 0, -1};
    for(int i = 0; i < 4; i++){
        //explore all 4 immediate neighbors
        int nr = r + dr[i];
        int nc = c + dc[i];
        if(nr >= 0 && nr <= n+1 && nc >= 0 && nc <= m+1){
            if(grid[nr][nc] == 0){
                grid[nr][nc] = 2;
                //if it's water, then we DFS there
                //but we'll set it to 2 so that we know it's been visited
                dfs(nr, nc);
            } else if(grid[nr][nc] == 1){
                //if it's 1, then we've found an edge to land.  so we increment ans by 1.
                ans++;
            }
        }
    }
}

int main(){
    cin >> n >> m;
    grid.push_back(vector<int>(m+2, 0));
    for(int i = 1; i < n+1; i++){
        grid.push_back(vector<int>(m+2, 0));
        for(int j = 1; j < m+1; j++){
            char a;
            cin >> a;
            if(a == '1'){
                grid[i][j] = 1;
            } else {
                grid[i][j] = 0;
            }
        }
    }
    grid.push_back(vector<int>(m+2));
    //debug code to print out the grid:
    // for(int i = 0; i < n+2; i++){
    //     for(int j = 0; j < m+2; j++){
    //         cout << grid[i][j];
    //     } cout << endl;
    // }
    grid[0][0] = 2;
    dfs(0, 0);
    cout << ans << endl;
    return 0;
}