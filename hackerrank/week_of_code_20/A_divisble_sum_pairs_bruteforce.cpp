#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, k;
    int as[100];
    cin >> n >> k;
    long ans;
    for(int i = 0; i < n; i++){
        cin >> as[i];
        for(int j = 0; j < i; j++){
            if((as[j] + as[i])%k == 0){
                ans++;
            }
        }
    }
    cout << ans;
    return 0;
}
