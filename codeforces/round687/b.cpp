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
        int n, k;
        cin >> n >> k;
        vector<int> cs(n);
        for(int i = 0; i < n; i++){
            cin >> cs[i];
        }
        int ans = 12345678;
        for(int i = 1; i <= 100; i++){
            int days = 0;
            for(int j = 0; j < n; j++){
                if (cs[j] != i) {
                    j+=k-1;
                    days++;
                }
            }
            ans = min(ans, days);
        }
        cout << ans << endl;
    }    
	return 0;
}