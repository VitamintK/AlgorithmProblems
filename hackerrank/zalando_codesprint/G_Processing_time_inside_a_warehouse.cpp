#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
typedef unsigned long long ull;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    //binary search -or- brute force
    //binary search would work 4sure, but i want to know if this is so doable that a brute force soln would work:
    ull N, M;
    ull emps[100000] = {0ull};
        cin >> N >> M;

    for(long long i = 0 ; i < M; i++){
        cin >> emps[i];
    }
    ull low = 0ull;
    ull high = 1000000000000000001ull;
    while(high > low){
        ull mid = low + (high - low + 1)/2;
        ull p = 0ull;
        for(long long i = 0; i < M; i++){
            p += mid/emps[i];
        }
        if(p < N){
            low = mid;
        } else{
            high = mid-1;
        }
    }
    cout << low+1ull;
    return 0;
}
