//author: pasha
#include<bits/stdc++.h>

using namespace std;


int main(){

    int n, m;
    cin >> n >> m;
    vector<int> eat(n);
    for(int i=0;i<n;i++)
        cin >> eat[i];

    vector<vector<int> > dp(n, vector<int>(m+1));

    for(int k = 0; k <= m; k++){
        dp[n-1][k] = min(k, eat[n-1]);
    }
    //for(int i=0;i<n;i++)
    //    dp[i][0] = 0;
    int best = 0;
    for(int i = n - 2; i >= 0;i--){
        for(int k = 0; k <= m ;k++){
            int ans = 0;

            ans = max(ans, dp[i+1][k * 2 / 3] + min(eat[i], k));
            //ans = max(ans, dp[i+1][k]);
            if(i+2 < n)
                ans = max(ans, dp[i+2][k] + min(eat[i], k));
            if(i + 3 < n)
                ans = max(ans, dp[i+3][m] + min(eat[i], k));
            dp[i][k] = ans;
            best = max(ans, best);
        }
    }
    cout << best << endl;

    // for(int i=0;i<n;i++){
    //     for(int j=0;j<=m;j++)
    //         cout<< dp[i][j] << " ";

    //     cout << endl;
    // }

    return 0;
}