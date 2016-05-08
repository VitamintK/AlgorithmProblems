#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
//ios::sync_with_stdio(false);

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int T;
    cin >> T;
    int k = T%7;
    if(k>2){
        k = 2;
    }
    cout << ((T+2)/7) << " " << (T/7)+k;
    
    return 0;
}
