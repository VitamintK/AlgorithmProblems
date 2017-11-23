#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
//this was a great problem: https://www.hackerrank.com/contests/w35/challenges/matrix-land

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, m;
    cin >> n >> m;
    vector<vector<int> > a(n, vector<int>(m));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            int x;
            cin >> x;
            a[i][j] = x;
        }
    }
    
    vector<int> prev(m);
    int ans = 0;
    for(int i = 0; i < n; i++){
        vector<vector<int>> l(2, vector<int>(m));
        vector<vector<int>> r(2, vector<int>(m));
        //l[0][i] means we haven't used a value from above yet
        //l[1][i] means we have
    //for this row, l[0 or 1][i] stores the max subarray that ends at i-1 (i.e. max subarray from the left up to but not including i)
    //r[0 or 1][i] stores the max subarray that begins at i+1 (i.e. max subarray from the right up to but not including i)
    //motiviation: we want to calculate prev[i], which represents the max score we can get if we reach i.  More specifically,
    //   we want to calculate prev[i][j], which is the max score we can get in the first i rows, if we "must take" A[i][j].
    //   We want this calculation because, in the next row, we are interested in the "crossing-over point" from row i to i+1, so if
    //   the crossing-over point is at column j, then we know that prev[i][j] is the best we could have done to get to a[i][j] and
    //   "cross over" there.  This reduces our problem to linear DP calculations per row, since the best way to get to every point in 
    //   the previous row is already decided.

        //fill up the vector l
        for(int j = 0; j < m; j++){
            if(j == 0){
                l[0][j] = 0;
                l[1][j] = prev[j];
            } else {
                l[0][j] = max(0, l[0][j-1]+a[i][j-1]);
                l[1][j] = max(l[1][j-1]+a[i][j-1], max(l[0][j-1]+a[i][j-1]+prev[j], prev[j]));
            }
        }
        //fill up the vector r
        for(int j = m-1; j >= 0; j--){
            if(j == m-1){
                r[0][j] = 0;
                r[1][j] = prev[j];
            } else {
                r[0][j] = max(0, r[0][j+1]+a[i][j+1]);
                r[1][j] = max(r[1][j+1]+a[i][j+1], max(r[0][j+1]+a[i][j+1]+prev[j], prev[j]));
            }
        }
        
        //calculate prev (our main DP table) from the values of l and r.
        ans = 0;
        for(int j = 0; j < m; j++){
            prev[j] = a[i][j] + max(r[0][j] + l[1][j], r[1][j] + l[0][j]);
            ans = max(ans, prev[j]);
        }
    }
    
    cout << ans << endl;
    return 0;
}
