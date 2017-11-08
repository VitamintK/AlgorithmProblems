#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int T;
    cin >> T;
    for(int t = 0; t < T; t++){
        int a,b,x;
        cin >> a >> b >> x;
        if(b-x+1 <= b/2){
            cout << -1 << endl;
            continue;
        }
        for(int n = b; n >= b-x+1; n--){
            cout << n << " ";
        }
        cout << endl;
    }
    return 0;
}
