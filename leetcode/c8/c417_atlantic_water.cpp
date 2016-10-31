#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
#include <utility>

using namespace std;

vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
        vector<pair<int, int> > ans;
        vector<vector<int> > pac;
                vector<vector<int> > atl;
        if(matrix.size() == 0){
            return vector<pair<int, int> >();
        }
        for(int i = 0; i < matrix.size(); i++){
            pac.push_back(vector<int>(matrix[0].size()));
                        atl.push_back(vector<int>(matrix[0].size()));

        }
        //pacific
        vector<pair<int, int> > to_explore;
        for(int col = 0; col < matrix[0].size(); col++){
            pac[0][col] = 1;
            to_explore.push_back(make_pair(0, col));
        }
        for(int row = 1; row < matrix.size(); row++){
            pac[row][0] = 1;
            to_explore.push_back(make_pair(row, 0));
        }
        while(!to_explore.empty()){
            pair<int, int> p = to_explore.back(); //row, col
            to_explore.pop_back();
            if(p.first - 1 >= 0){
                if(pac[p.first - 1][p.second] == 0){
                    if(matrix[p.first - 1][p.second] >= matrix[p.first][p.second]){
                        pac[p.first-1][p.second] = 1;
                        to_explore.push_back(make_pair(p.first-1, p.second));
                    }else {
                        //pac[p.first-1][p.second] = -1;
                    }
                }
            }
            if(p.second + 1 < matrix[0].size()){
                if(pac[p.first][p.second + 1] == 0){
                    if(matrix[p.first][p.second + 1] >= matrix[p.first][p.second]){
                        pac[p.first][p.second + 1] = 1;
                        to_explore.push_back(make_pair(p.first, p.second + 1));
                    }else {
                        //pac[p.first][p.second + 1] = -1;
                    }
                }
            }
            if(p.first + 1 < matrix.size()){
                if(pac[p.first + 1][p.second] == 0){
                    if(matrix[p.first + 1][p.second] >= matrix[p.first][p.second]){
                        pac[p.first+1][p.second] = 1;
                        to_explore.push_back(make_pair(p.first+1, p.second));
                    }else {
                        //pac[p.first+1][p.second] = -1;
                    }
                }
            }
            if(p.second - 1 >= 0){
                if(pac[p.first][p.second - 1] == 0){
                    if(matrix[p.first][p.second - 1] >= matrix[p.first][p.second]){
                        pac[p.first][p.second - 1] = 1;
                        to_explore.push_back(make_pair(p.first, p.second - 1));
                    }else {
                        //pac[p.first][p.second - 1] = -1;
                    }
                }
            }
        }
        //atlantic
        for(int col = 0; col < matrix[0].size(); col++){
            atl[matrix.size() - 1][col] = 1;
            to_explore.push_back(make_pair(matrix.size() - 1, col));
        }
        for(int row = 0; row < matrix.size(); row++){
            atl[row][matrix[0].size() - 1] = 1;
            to_explore.push_back(make_pair(row, matrix[0].size() - 1));
        }
        while(!to_explore.empty()){
            pair<int, int> p = to_explore.back(); //row, col
            to_explore.pop_back();
            if(p.first - 1 >= 0){
                if(atl[p.first - 1][p.second] == 0){
                    if(matrix[p.first - 1][p.second] >= matrix[p.first][p.second]){
                        atl[p.first-1][p.second] = 1;
                        to_explore.push_back(make_pair(p.first-1, p.second));
                    }else {
                        //atl[p.first-1][p.second] = -1;
                    }
                }
            }
            if(p.second + 1 < matrix[0].size()){
                if(atl[p.first][p.second + 1] == 0){
                    if(matrix[p.first][p.second + 1] >= matrix[p.first][p.second]){
                        atl[p.first][p.second + 1] = 1;
                        to_explore.push_back(make_pair(p.first, p.second + 1));
                    }else {
                        //atl[p.first][p.second + 1] = -1;
                    }
                }
            }
            if(p.first + 1 < matrix.size()){
                if(atl[p.first + 1][p.second] == 0){
                    if(matrix[p.first + 1][p.second] >= matrix[p.first][p.second]){
                        atl[p.first+1][p.second] = 1;
                        to_explore.push_back(make_pair(p.first+1, p.second));
                    }else {
                        //atl[p.first+1][p.second] = -1;
                    }
                }
            }
            if(p.second - 1 >= 0){
                if(atl[p.first][p.second - 1] == 0){
                    if(matrix[p.first][p.second - 1] >= matrix[p.first][p.second]){
                        atl[p.first][p.second - 1] = 1;
                        to_explore.push_back(make_pair(p.first, p.second - 1));
                    }else {
                        //atl[p.first][p.second - 1] = -1;
                    }
                }
            }
        }
        //ok
        for(int i = 0; i < matrix.size(); i++){
            for(int j =0 ; j < matrix[0].size(); j++){
                if(atl[i][j] == 1 && pac[i][j] == 1){
                    ans.push_back(make_pair(i, j));
                }
            }
        }
        return ans;
    }

int main(){
    vector<vector<int> > i;
    vector<int> v;
    v.push_back(3);
    v.push_back(3);
    v.push_back(3);
    v.push_back(3);
    v.push_back(3);
    v.push_back(3);
    i.push_back(v);
    vector<int> w;
    w.push_back(3);
    w.push_back(0);
    w.push_back(3);
    w.push_back(3);
    w.push_back(0);
    w.push_back(3);
    vector<int> x;
    x.push_back(3);
    x.push_back(3);
    x.push_back(3);
    x.push_back(3);
    x.push_back(3);
    x.push_back(3);
    i.push_back(v);
    i.push_back(w);
    i.push_back(x);
    pacificAtlantic(i);
}