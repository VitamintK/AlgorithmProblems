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
    ll n, k;
    cin >> n >> k;
    ll x, y;
    cin >> x >> y;
    set<pair<ll,ll>> board;
    ll xx, yy;
    for(ll i = 0; i < k; i++){
        cin >> xx >> yy;
        board.insert(make_pair(xx-1,yy-1));
    }
    ll ans = 0;
    for(ll col = x-1; col < n && board.count(make_pair(col,y-1)) < 1; col++){
        ans++;
    }
    for(ll col = x-1; col >=0 && board.count(make_pair(col,y-1)) < 1; col--){
        ans++;
    }
    for(ll col = x-1, row = y-1; col < n && row < n && row >= 0 && col >= 0 && board.count(make_pair(col,row)) < 1; col++, row++){
        ans++;
    }
    for(ll col = x-1, row = y-1; col < n && row < n && row >= 0 && col >= 0 && board.count(make_pair(col,row)) < 1; col--, row++){
        ans++;
    }
    for(ll col = x-1, row = y-1; col < n && row < n && row >= 0 && col >= 0 && board.count(make_pair(col,row)) < 1; col++, row--){
        ans++;
    }
    for(ll col = x-1, row = y-1; col < n && row < n && row >= 0 && col >= 0 && board.count(make_pair(col,row)) < 1; col--, row--){
        ans++;
    }
    for(ll col = x-1, row = y-1; col < n && row < n && row >= 0 && col >= 0 && board.count(make_pair(col,row)) < 1; row--){
        ans++;
    }
    for(ll col = x-1, row = y-1; col < n && row < n && row >= 0 && col >= 0 && board.count(make_pair(col,row)) < 1; row++){
        ans++;
    }
    cout << ans - 8 << endl;
    return 0;
}
