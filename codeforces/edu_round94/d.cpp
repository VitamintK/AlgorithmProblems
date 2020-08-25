#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <utility>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int T;
    cin >>T;
    for(int t = 0; t < T; t++){
        int n;
        cin >> n;
        vector<int> as(n);
        vector<vector<int>> pre(n+1, vector<int>(n+1, 0));
        vector<vector<int>> suf(n+1, vector<int>(n+1, 0));
        for(int i = 0; i < n; i++){
            cin >> as[i];
        }
        for(int i = 1; i <= n; i++) {
            for(int j = 0; j <= n; j++){
                pre[i][j] = pre[i-1][j];
                if (as[i-1] == j) {
                    pre[i][j]++;
                }
            }
        }
        for(int i = n-2; i >=0; i--) {
            for(int j = 0; j <= n; j++){
                suf[i][j] = suf[i+1][j];
                if (as[i+1] == j) {
                    suf[i][j]++;
                }
            }
        }
        ll ans = 0;
        for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n; j++) {
                // cout << i << " " << j << " " << suf[j][as[i]] * pre[i][as[j]] << endl;
                ans += suf[j][as[i]] * pre[i][as[j]];
            }
        }
        cout << ans << endl;
    }
	return 0;
}