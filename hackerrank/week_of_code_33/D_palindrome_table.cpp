#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

#define ll long long


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, m;
    cin >> n >> m;
    bool swp = n > m;
    vector<vector<int>> grid(min(n,m), vector<int>(max(n,m)));
    int tmp;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> tmp;
            if(swp){
                grid[j][i] = (1 << tmp);
            } else {
                grid[i][j] = (1 << tmp);
            }
        }
    }
    if(swp){
        swap(n,m);
    }
    vector<vector<int>> num_of_nonzero (n, vector<int>(m));
    vector<vector<int>> column_pre (n+1, vector<int>(m));
    //column_pre[i][j] is XOR(grid[0][j], ... grid[i-1][j])
    for(int col = 0; col < m; col++){
        for(int row = 1; row < n+1; row++){
            column_pre[row][col] = grid[row-1][col] ^ column_pre[row-1][col];
            if(grid[row-1][col] != 1){
                num_of_nonzero[row][col] = num_of_nonzero[row-1][col] + 1;
            } else {
                num_of_nonzero[row][col] = num_of_nonzero[row-1][col];
            }
        }
    }
    int ans = 0;
    int x0, y0, x1, y1;
    int running_bitmask = 0;
    vector<int> leftmost_bitmask(1030); //tracks index of leftmost bitmask
    for(int top = 0; top < n; top++){
        for(int bot = top; bot < n; bot++){
            running_bitmask = 0;
            for(int i = 0; i < (1<<10); i++){
                leftmost_bitmask[i] = -1;
            }
            leftmost_bitmask[0] = 0;
            for(int i = 0; i < m; i++){
                running_bitmask = running_bitmask ^ column_pre[top][i] ^ column_pre[bot+1][i];
                for(int i = 0; i < 10; i++){
                    
                }
            }
        }
    }
    return 0;
}
