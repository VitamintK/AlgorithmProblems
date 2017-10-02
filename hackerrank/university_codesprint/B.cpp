#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#define ll long long
using namespace std;


int main(){
    ll n;
    ll k;
    cin >> n >> k;
    vector<ll> x(n);
    //ll a;
    for(ll x_i = 0;x_i < n;x_i++){
        cin >> x[x_i];
    }
    sort(x.begin(), x.end());
    ll need_to_cover = x[0];
    ll cur_transmitter = -100000;
    ll ans = 0;
    for(ll i = 0; i < n; i++){
        if(x[i] > cur_transmitter + k && need_to_cover + k < x[i] && cur_transmitter > -1){
            need_to_cover = x[i];
            //cout <<"need to cover "<< x[i] << endl;
        }
        if(i < n && x[i+1] > need_to_cover+k && x[i] <= need_to_cover + k){
            cur_transmitter = x[i];
            //cout <<"transmitter on " << x[i] << endl;
            ans++;
        }

    }
    if(x[n-1] > cur_transmitter+k){
        ans++;
    }
    cout << ans;
    return 0;
}
