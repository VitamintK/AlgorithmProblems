#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    //4 am to 4:21 am
    long long n;
    int k;
    long long as[100001];
    long long mods[100] = {0};
    cin >> n >> k;
    
    for(long long i = 0; i < n; i++){
        cin >> as[i];
        mods[as[i]%k]++;
    }
    
    long long ans = 0;
    for(int i = 1; i < (k+2)/2; i++){
        if(i * 2 == k){
            if(mods[i] > 0){
                ans++;
            }
        } else {
            ans+=max(mods[i], mods[k-i]);
        }
    }
    if(mods[0] > 0){
        ans++;
    }
    cout << ans;
    return 0;
}
