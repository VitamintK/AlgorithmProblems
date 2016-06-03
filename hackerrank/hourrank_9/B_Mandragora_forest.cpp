#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool flag;
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    long long T;
    cin >> T;
    long long N;
    long long as[100001];
            long long totals[100001];
    for(long long i = 0; i < T; i++){
        flag = false;
        cin >> N;
        
        for(long long j = 0; j < N; j++){
            cin >> as[j];
        }
        sort(as, as+N);
        totals[N-1] = as[N-1];
        for(long long b = N-2; b >= 0; b--){
            totals[b] = totals[b+1] + as[b];
        }
        for(long long b = 0; b < N-1; b++){
            if((b+1)*as[b] > totals[b+1]){
                cout << (b+1)*totals[b] << endl;
                flag = true;
                break;
            }
        }
        if(!flag){
        cout << N * totals[N-1] << endl;
        }
    }
    return 0;
}
