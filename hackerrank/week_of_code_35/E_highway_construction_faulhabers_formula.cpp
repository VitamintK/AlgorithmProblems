//We want to find the result of the sum of i^k for i from 0 to n-1, but minus 1, since the closest city is not needed.

//Here we implement Faulhaber's formula by using Bernoulli numbers.
//There is also an additional complication of doing all our arithmetic mod 1e9+9,
//so we also have to use extended euclidean to find and multiply by mod inverses instead of doing regular ol division.

//First we find all the Bernoulli numbers.  To do this, we need to quickly get (i choose j), so we precalculate those
//  using Pascal's identity.
//Then we implement Faulhaber's formula, which is an summation of k expressions, so we do it in O(k).
//  To do this, we also precalculate all the powers of (n-1) we'll need.
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

long long MOD = 1000000009;

long long mod_inverse(long long a, long long m){
    long long x;
    long long y;
    long long xx = y =  0;
    long long yy = x = 1;
    while(m){
        long long q = a/m;
        long long t = m; m = a%m; a = t;
        t = xx; xx = x - q*xx; x = t;
        t = yy; yy = y - q*yy; y = t;
    }
    return ((x%MOD)+MOD)%MOD;
}

long long mod(long long a){
    return ((a%MOD)+MOD)%MOD;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int Q;
    cin >> Q;

    //first we fill out the combos table.  combos[i][j] := (i choose j)
    //Pascal's identity: https://en.wikipedia.org/wiki/Pascal%27s_rule
    vector<vector<long long> > combos(1006, vector<long long>(1006, 0ll));
    for(int i = 0; i < 1006; i++){
        for(int j = 0; j < 1006; j++){
            if(j > i){
                combos[i][j] = 0ll;
            } else if (j == 0){
                combos[i][j] = 1ll;
            } else {
                combos[i][j] = (combos[i-1][j-1] + combos[i-1][j])%MOD;
            }
        }
    }
    
    //then we calculate the first 1005 bernoulli numbers.  we use mod_inverse instead of division.
    //Recursive formula for B_n given all B_i for i < n: https://en.wikipedia.org/wiki/Bernoulli_number#Recursive_definition
    vector<long long> BERNOULLI;
    
    for(int m = 0; m < 1005; m++){
        long long bern = 1; //"bern" should definitely be bernoulli's new nickname
        for(int k = 0; k < m; k++){
            bern -= mod(mod(combos[m][k] * BERNOULLI[k]) * mod_inverse(m - k + 1, MOD));
            bern = mod(bern);
        }
        BERNOULLI.push_back(mod(bern));
    }
    
    //Finally, we process the queries.
    for(int i = 0; i < Q; i++){
        long long n, k;
        cin >> n >> k;
        
        long long ans = 0;
        
        //since faulhaber's formula contains n^(p+1-j), we preprocess all powers of n.  (in this case, n-1, not n)
        vector<long long> powers;
        powers.clear();
        powers.push_back(1);
        for(long long j = 1; j < k+3; j++){
            powers.push_back(mod(powers.back() * mod(n-1)));
        }
        
        //Then, we implement Faulhaber's formula: https://en.wikipedia.org/wiki/Faulhaber%27s_formula#Summae_Potestatum
        for(long long j = 0; j <= k; j++){
            ans += mod(mod(combos[k+1][j] * BERNOULLI[j]) * powers[k+1-j]); 
            ans = mod(ans);
        }
        ans = mod(ans * mod_inverse(k + 1, MOD) - 1);

        //Print the answer
        cout.precision(0);
        if(n == 1){
            cout << 0 << endl;
        } else {
            cout << fixed << ans << endl;
        }
    }
    return 0;
}
