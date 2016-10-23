#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    ll n, k;
    cin >> n >> k;
    vector<ll> cs;
    ll dp[1][10001] = {0};
    ll dpmax[1][10001] = {0};
    ll c;
    for(ll i = 0; i < n; i++){
        cin >> c;
        cs.push_back(c);
    }
    //set dp[0][0]
    ll mincostind = 0;
    for(ll i = 0; i < min(n,k+1); i++){
        if(cs[i] < cs[mincostind])
            mincostind = i;
    }
    dpmax[0][0] = mincostind+k;
    dp[0][0] = cs[mincostind]; 
    for(ll i = 1; i < n; i++){
        if(dpmax[0][i-1] >= i){
            dpmax[0][i] = dpmax[0][i-1];
            dp[0][i] = dp[0][i-1];
            continue;
        }
        mincostind = i;
        dp[0][i] = dp[0][i-1] + cs[mincostind];
        for(ll j = max(0ll,i-k); j < min(n, i+k+1); j++){
            if(j - k <= 0){
                if(cs[j] < dp[0][i]){
                    mincostind = j;
                    dp[0][i] = cs[j];
                }
            } else {
                if(cs[j]+dp[0][j-k-1] < dp[0][i]){
                    mincostind = j;
                    dp[0][i] = cs[j] + dp[0][j-k-1];
                }
            }
        }
        dpmax[0][i] = mincostind+k;
        //dp[0][i] = cs[mincostind] + dp[0][i-1];
    }
    for(ll i = 0; i < n; i++){
        //cout << dp[0][i] << " ";
    }
    //cout << endl;
    cout << dp[0][n-1] << endl;
    return 0;
}
