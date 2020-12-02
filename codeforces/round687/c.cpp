#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <utility>
#include <iomanip>
#include <cmath>

#define ll long long
#define ull unsigned long long
using namespace std;

ll MOD = 1000000007;

int main(){
	std::ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int t = 0; t<T; t++){
        int n, p, k;
        cin >> n >> p >> k;
        p--;
        string s;
        cin >> s;
        int x, y;
        cin >> x >> y;
        ll ans = 12345678912345678;
        vector<int> costs(n);
        for(int i = n-1;i>=p;i--){
            ll cost = (i-p)*y;
            ll platforms = 0;
            if( s[i] == '0' ){
                platforms += x;
            }
            if(i+k<n){
                platforms += costs[i+k];
            }
            costs[i] = platforms;
            cost += platforms;
            ans = min(ans, cost);
            // cout << i << " " << cost << endl;
        }
        cout << ans << endl;
    }    
	return 0;
}