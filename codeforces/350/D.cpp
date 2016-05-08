#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <signal.h>
using namespace std;
//ios::sync_with_stdio(false);
long long n, k;

long long as[100001];
long long bs[100001];
//long long usedk;
//long long make;
bool can_make(long long make){
    //long long usek = k - usedk;
    long long usek = k;
    long long en;
    for(long i = 0; i < n; i++){
        en = (make)*as[i] - bs[i];
        if(en > 0){
            usek -= en;
        }
        if(usek < 0){
            return false;
        }
    }
    return true;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    cin >> n >> k;
    for(long long i = 0; i < n; i++){
        cin >> as[i];
    }
    for(long long i = 0; i < n; i++){
        cin >> bs[i];
    }
    //calculate the upper bound
    long long maxk = 0;
    for(long i = 0; i < n; i++){
        maxk = max((bs[i]+k)/as[i], maxk);
    }
    maxk = maxk + 1;
    //
    //long long maxk = k;
    long long mid = maxk/2;
    long long mink = 0;
    bool cm;
    if(!can_make(0)){
        cout << 0;
        as[10000000000000] = 1;
        raise(SIGSEGV);
        return 0;
    }
    if(!can_make(1)){
        cout << 0;
        return 0;
    }
    while(true){
        cm = can_make(mid);
        if(cm && !can_make(mid+1)){
            cout << mid;
            return 0;
        }
        else if(!cm){
            //cant make this much
            maxk = mid-1;
        } else {
            mink = mid + 1;
        } 
        mid = (mink + maxk)/2;
    }

    return 0;
}
