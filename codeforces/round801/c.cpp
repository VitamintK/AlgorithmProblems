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

int main(){
	std::ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int t = 0; t < T; t++){
        int n, m;
        cin >> n >> m;
        vector<vector<int> > grid(n, vector<int>(m));
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                cin >> grid[i][j];
            }
        }
        if ((n+m-1)%2 != 0){
            cout << "NO" << endl;
            continue;
        }
        vector<vector<int> > hi(n, vector<int>(m, -99999999));
        vector<vector<int> > lo(n, vector<int>(m, 99999999));
        hi[0][0] = grid[0][0];
        lo[0][0] = grid[0][0];
        for(int i =0; i < n; i++){
            for(int j =0; j < m; j++){
                if (i > 0) {
                    hi[i][j] = max(hi[i][j], hi[i-1][j] + grid[i][j]);
                    lo[i][j] = min(lo[i][j], lo[i-1][j] + grid[i][j]);
                }
                if (j > 0) {
                    hi[i][j] = max(hi[i][j], hi[i][j-1] + grid[i][j]);
                    lo[i][j] = min(lo[i][j], lo[i][j-1] + grid[i][j]);
                }
            }
        }
        if (hi[n-1][m-1] >= 0 && lo[n-1][m-1] <= 0) {
            // cout << hi[n-1][m-1] << " " << lo[n-1][m-1] << endl;
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    } 
	return 0;
}