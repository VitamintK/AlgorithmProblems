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
#include <set>
#include <queue>
#include <utility>
#define ll long long
using namespace std;

int n, k;

bool can(ll max_pain, vector<ll> xs) {
    // cout << max_pain << " " << n << " " << k << endl;
    int used = 0;
    for (int i = 1; i < xs.size(); i++) {
        ll diff = xs[i] - xs[i-1];
        used += (diff + max_pain - 1)/max_pain - 1;
    }
    // cout << used << endl;
    return used <= k;
}

int main(){
    std::ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++){
        cin >> n >> k;
        vector<ll> xs(n);
        for(int i = 0; i < n; i++){
            cin >> xs[i];
        }
        ll lo = 0;
        ll hi = 1123456789;
        while (hi-1 > lo) {
            ll mid = (lo+hi)/2;
            // cout << "lo: " << lo << ", hi: " << hi << ", mid: " << mid << endl;
            if (can(mid, xs)) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        cout << "Case #" << t+1 << ": " << hi << endl;
    }
}