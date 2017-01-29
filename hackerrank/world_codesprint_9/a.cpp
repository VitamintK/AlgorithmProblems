#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    ll n;
    cin >> n;
    for(ll i = 0; i < n; i++){
        ll a;
        cin >> a;
        if(a < 38){
            cout << a << endl;
        } else {
            if(a%5 >= 3){
                a = a + 5-(a%5);
            }
            cout << a << endl;
        }
    }
    return 0;
}
