#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
using namespace std;

int main(){
    std::ios::sync_with_stdio(false);
    long r, c;
    cin >> r >> c;
    vector<vector<char> > grid(r, vector<char>(c));
    for(long i = 0; i < r; i++){
        for(long j = 0; j < c; j++){
            cin >> grid[i][j];
        }
    }
    for(long col = 0; col < c; col++){
        long obstacle = r-1;
        for(long row = r-1; row >= 0; row--){
            if(grid[row][col] == 'a'){
                grid[row][col] = '.';
                grid[obstacle][col] = 'a';
                obstacle--;
            } else if(grid[row][col] == '#'){
                obstacle = row-1;
            }
        }
    }
    for(long i = 0; i < r; i++){
        for(long j = 0; j < c; j++){
            cout << grid[i][j];
        }
        cout << endl;
    }
    return 0;
}