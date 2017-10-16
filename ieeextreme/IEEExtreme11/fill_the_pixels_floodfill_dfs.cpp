#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++){
        int w, h;
        cin >> w >> h;
        char input;
        vector<vector<int>> grid1(h, vector<int>(w));
        vector<vector<int>> grid2(h, vector<int>(w));
        vector<vector<int>> grid3(h, vector<int>(w));

        for(int r = 0; r < h; r++){
            for(int c = 0; c < w; c++){
                cin >> input;
                if(input == '1'){
                    grid1[r][c] = 1;
                    grid2[r][c] = 1;
                    grid3[r][c] = 1;
                } else {
                    grid1[r][c] = 0;
                    grid2[r][c] = 0;
                    grid3[r][c] = 0;
                }
            }
        }
        
        vector<int> ans;
        //
        int sub_ans = 0;
        for(int r = 0; r < h; r++){
            for(int c = 0; c < w; c++){
                if(grid1[r][c] == 1){
                    sub_ans++;
                    vector<pair<int, int>> stack;
                    stack.push_back(make_pair(r,c));
                    while(!stack.empty()){
                        pair<int,int> ex = stack.back();
                        int R, C;
                        R = ex.first;
                        C = ex.second;
                        stack.pop_back();
                        grid1[R][C] = 0;
                        vector<int> dc = {-1, 0, 1, 0};
                        vector<int> dr = {0, -1, 0, 1};
                        for(int i = 0; i < 4; i++){
                            int new_r = R + dr[i];
                            int new_c = C + dc[i];
                            if(new_r < 0 || new_r >= h || new_c < 0 || new_c >= w){
                                continue;
                            }
                            if(grid1[new_r][new_c] != 0){
                                grid1[new_r][new_c] = 0;
                                stack.push_back(make_pair(new_r,new_c));
                            }
                        }
                    }
                }
            }
        }
        cout << sub_ans << " ";
        //
        sub_ans = 0;
        for(int r = 0; r < h; r++){
            for(int c = 0; c < w; c++){
                if(grid2[r][c] == 1){
                    sub_ans++;
                    vector<pair<int, int>> stack;
                    stack.push_back(make_pair(r,c));
                    while(!stack.empty()){
                        pair<int,int> ex = stack.back();
                        int R, C;
                        R = ex.first;
                        C = ex.second;
                        stack.pop_back();
                        grid2[R][C] = 0;
                        vector<int> dc = {-1, 1, -1, 1};
                        vector<int> dr = {-1, 1, 1, -1};
                        for(int i = 0; i < 4; i++){
                            int new_r = R + dr[i];
                            int new_c = C + dc[i];
                            if(new_r < 0 || new_r >= h || new_c < 0 || new_c >= w){
                                continue;
                            }
                            if(grid2[new_r][new_c] != 0){
                                grid2[new_r][new_c] = 0;
                                stack.push_back(make_pair(new_r,new_c));
                            }
                        }
                    }
                }
            }
        }
        cout << sub_ans << " ";
        //
        sub_ans = 0;
        for(int r = 0; r < h; r++){
            for(int c = 0; c < w; c++){
                if(grid3[r][c] == 1){
                    sub_ans++;
                    vector<pair<int, int>> stack;
                    stack.push_back(make_pair(r,c));
                    while(!stack.empty()){
                        pair<int,int> ex = stack.back();
                        int R, C;
                        R = ex.first;
                        C = ex.second;
                        stack.pop_back();
                        grid3[R][C] = 0;
                        vector<int> dc = {-1, 0, 1, 1, 1, 0, -1, -1};
                        vector<int> dr = {-1, -1, -1, 0, 1, 1, 1, 0};
                        for(int i = 0; i < 8; i++){
                            int new_r = R + dr[i];
                            int new_c = C + dc[i];
                            if(new_r < 0 || new_r >= h || new_c < 0 || new_c >= w){
                                continue;
                            }
                            if(grid3[new_r][new_c] != 0){
                                grid3[new_r][new_c] = 0;
                                stack.push_back(make_pair(new_r,new_c));
                            }
                        }
                    }
                }
            }
        }
        cout << sub_ans << endl;
    }
    return 0;
}