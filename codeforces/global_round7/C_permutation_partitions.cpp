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

bool is_max(int i, int n, int k){
    return i > n-k;
}

int main(){
    std::ios::sync_with_stdio(false);
    int n, k;
    cin >> n >> k;
    vector<int> ps(n);
    for(int i = 0; i < n; i++){
        cin >> ps[i];
    }
    ll ans = 1;
    int last_pos = -1;
    for (int i =0; i < n; i++){
        if (is_max(ps[i], n, k)){
            if (last_pos == -1) {
                last_pos = i;
            } else {
                ans *= i - last_pos;
                ans %= 998244353;
                last_pos = i;
            }
        }
    }
    ll ans0 = 0;
    for(int i = n; i > n-k; i--){
        ans0 += i;
    }
    cout << ans0 << " " << ans << endl;
}