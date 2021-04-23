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

int n, m, K;
vector<vector<vector<int> > > memo;
vector<vector<int> > horiz;
vector<vector<int> > vert;

int gett(int k, int r, int c){
    // cout << k << " " << r << " " << c << endl;
    if(k == 0){
        return 0;
    }
    if(memo[r][c][k] != -1){
        // cout << memo[r][c][k];
        return memo[r][c][k];
    }
    int ans = 112345678;
    if(r > 0){
        ans = min(ans, vert[r-1][c]+gett(k-1,r-1,c));
    }
    if(r < n-1){
        ans = min(ans, vert[r][c]+gett(k-1,r+1,c));
    }
    if(c > 0){
        ans = min(ans, horiz[r][c-1]+gett(k-1,r,c-1));
    }
    if(c < m-1){
        ans = min(ans, horiz[r][c]+gett(k-1,r,c+1));
    }
    memo[r][c][k] = ans;
    // cout << k << " " << r << " " << c << endl;
    return ans;
}

int main(){
	std::ios::sync_with_stdio(false);
    cin >> n >> m >> K;

    horiz.resize(0);
    vert.resize(0);
    for(int i = 0; i < n; i++){
        vector<int> h(m-1);
        for(int j = 0; j < m-1; j++){
            cin >> h[j];
        }
        horiz.push_back(h);
    }
    for(int i = 0; i < n-1; i++){
        vector<int> v(m);
        for(int j = 0; j < m; j++){
            cin >> v[j];
        }
        vert.push_back(v);
    }
    vector<vector<int> > anss(n, vector<int>(m, -1));
    if(K%2 == 0){
        memo = vector<vector<vector<int> > >(n, vector<vector<int>>(m, vector<int>(K/2 + 1, -1)));
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                anss[i][j] = gett(K/2, i, j)*2;
            }
        }
    }
    for(int i = 0; i<n; i++){
        for(int j=0; j<m; j++){
            cout << anss[i][j];
            if(j<m-1){cout << " ";}
        }
        cout << endl;
    }
	return 0;
}