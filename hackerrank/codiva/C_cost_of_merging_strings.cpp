//easy DP. :P
// fun problem.  I fucked up and learned about putting big-ass arrays in the heap instead of stack, and thinking through
// what the base case truly is.  should have used 1-based indexing and reserved 0 for the true basecases (the null cases).
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
    int DP[360][360][360] = {{{0}}};


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, m, k;
    cin >> n >> m >> k;
    string s, t;
    cin >> s >> t;
    //cout << s << " " << t << endl;
    //cout << DP[0][0][0];
    int ans = 1234566;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            for(int l = 0; l <= 355; l++){
                DP[i][j][l] = 1234567;
                if(i == 0 && j == 0 && l == 0){ //base case
                    DP[i][j][l] = 0;
                }
               if((i == 0 || j == 0) && l == 1){ //base case 
                    DP[i][j][l] = (s[i]-'a')^(t[j]-'a');
                }
                if(l > 0 && i > 0 && j > 0 && DP[i-1][j-1][l-1] < 1234567){ //use these letters
                    DP[i][j][l] = DP[i-1][j-1][l-1] + ((s[i]-'a')^(t[j]-'a'));
                }
                if(i > 0 && DP[i-1][j][l] < 1234567){ //just use s
                    DP[i][j][l] = min(DP[i][j][l], DP[i-1][j][l]);
                }
                if(j > 0 && DP[i][j-1][l] < 1234567){//just use t
                    DP[i][j][l] = min(DP[i][j][l], DP[i][j-1][l]);
                }
                
                if(i == n-1 && j == m-1 && l >= k){
                    ans = min(ans, DP[i][j][l]);
                }
            }
        }
    }
    if(k > min(n,m)){
        cout << -1 << endl;
    } else {
        cout << ans << endl;
    }
    return 0;
}
