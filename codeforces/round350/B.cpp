#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    //ios::sync_with_stdio(false);
ios_base::sync_with_stdio(false);
long long robots[100001];
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    long long N, K;
    cin >> N >> K;
    for(long i = 0; i < N; i++){
        cin >> robots[i];
    }

    for(long i = 0; i < N; i++){
        if(K-i <= 0){
            cout << robots[K-1];
            return 0;
        } else {
            K = K - (i+1);
            //cout << K << endl;
        }
       
    }
    return 0;
}