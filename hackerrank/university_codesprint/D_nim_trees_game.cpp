#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define ll long long

ll nim(ll num){
    if(num == 0){
        return 0;
    }
    if(num == 1){
        return 1;
    }
    if(num == 2){
        return 0;
    }
    if(num %2 == 0){
        return 2;
    }
    return 1;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    ll g;
    cin >> g;
    for(ll i = 0; i < g; i++){
        ll n;
        cin >> n;
        ll ans = 0;
        ll m, k;
        for(ll j = 0; j < n; j++){
            cin >> m >> k;
            ans^=nim(m);
        }
        cout << (ans==0?"BEN":"BOB") << endl;
    }
    return 0;
}
