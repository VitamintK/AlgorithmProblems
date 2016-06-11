#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    long long N, W, H, D;
    cin >> N >> W >> H >> D;
    
    long long ok = 10000000000;
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= ((N+i-1)/i); j++){
            for(int k = 1; k <= (N+i*j-1)/(i*j); k++){
                if(k*i*j >= N){
                    ok = min(ok, 2 * (W*i*H*j + W*i*D*k + H*j*D*k));
                }
            }
        }
    }
    cout << ok;
    return 0;
}
