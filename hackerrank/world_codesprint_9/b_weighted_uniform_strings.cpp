#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;
#define ll long long

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    string s;
    cin >> s;
    set<ll> values;
    ll cur = s[0] - 'a' + 1;
    values.insert(cur);
    for(ll i  = 1; i < s.length(); i++){
        if(s[i] == s[i-1]){
            cur += s[i] - 'a' + 1;
        }
        else{
            cur = s[i] - 'a' + 1;
        }
        values.insert(cur);
    }
    ll n;
    cin >> n;
    for(ll i = 0; i < n; i++){
        ll a;
        cin >> a;
        if(values.count(a) > 0){
            cout <<"Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
    return 0;
}
