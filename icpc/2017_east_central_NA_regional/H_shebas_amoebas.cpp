#include<bits/stdc++.h>

using namespace std;

int main(){
    int m, n;
    cin >> m >> n;
    vector<vector<int> > g(100, vector<int>(100));
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            char x;
            cin >> x;
            if(x == '#'){
                g[i][j] = 1;
            } else{
                g[i][j] = 0;
            }
        }
    }
    int ans = 0;
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            vector<pair<int, int>> stack;
            if(g[i][j] == 1){
                ans++;
                stack.push_back(make_pair(i,j));
                while(!stack.empty()){
                    pair<int, int> ex = stack.back();
                    stack.pop_back();
                    if(g[ex.first][ex.second] != 1){
                        continue;
                    }
                    g[ex.first][ex.second] = 2;
                    for(int dx = -1; dx <= 1; dx++){
                        for(int dy = -1; dy <= 1; dy++){
                            if(dx == 0 && dy == 0){
                                continue;
                            }
                            int nx = ex.second + dx;
                            int ny = ex.first + dy;
                            if(nx >= 0 && nx < n && ny >= 0 && ny < m && g[ny][nx] == 1){
                                stack.push_back(make_pair(ny,nx));
                            }
                        }
                    }
                }
            }
            
        }

    }
    cout << ans << endl;
    return 0;
}