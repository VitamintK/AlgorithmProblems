#include <iostream> 
#include <string> 
#include <set> 
#include <map> 
#include <stack> 
#include <queue> 
#include <vector> 
#include <utility> 
#include <iomanip> 
#include <sstream> 
#include <bitset> 
#include <cstdlib> 
#include <iterator> 
#include <algorithm> 
#include <cmath>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int n, m;
	cin >> n >> m;
    vector<int> ans(100001,-1);
    vector<int> DP(100001,-1);
    ans[0] = 0;
    DP[0] = 0;
    for(int i = 0; i < n; i++){
        ll t, x, y;
        cin >> t >> x >> y;
        if (t==1){
            x = (x+99999)/100000;
        }
        for (int j = 0; j <= m; j++) {
            if(DP[j] != -1){
                DP[j] = y;
            }
        }
        for(int j = 0; j<=m; j++){
            if(DP[j] > 0) {
                ll targ;
                if(t == 1){
                    targ = j+x;
                } else {
                    targ = ceil((double)j * (double)x / 100000.0);
                }
                if (targ <= m) {
                    DP[targ] = max(DP[j]-1, DP[targ]);
                    if (ans[targ] == -1){
                        ans[targ] = i+1;
                    }
                }
            }
        }
    }
    for (int i = 1; i <= m; i++) {
        cout << ans[i] << " ";
    }
    cout << endl;
	return 0;
}