#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
//I READ THE EDITORIAL BEFORE DOING THIS PROBLEM.
//I still do not understand why (i.e. i can not think of a proof for why) there can be no absolute permutation 
//when n is not divisible by 2*k.
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int T;
    long n, k;
    cin >> T;
    long ans[100000];
    for(int i = 0; i < T; i++){
        cin >> n >> k;
       // for(int j = 0; j < n; j++){
            //ans[j] = j+1;
       // }
        if(k == 0){
            for(int j = 0; j < n; j++){
                cout << j+1 << " "; 
            }
            cout << endl;
            continue;
        }
        if(n%(k*2) != 0){
            cout << -1 << endl;
            continue;
        }
        int up = 1;
        for(int j = 1; j <= n; j++){
            cout << j + (k)*up << " ";
            if(j%k == 0){
                up = up*-1;
            }
        }
        cout << endl;
    }
    return 0;
}
