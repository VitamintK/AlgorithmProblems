#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <utility>
#include <iomanip>

#define ll long long
#define ull unsigned long long
using namespace std;

ll MOD = 1000000007;

int main(){
	std::ios::sync_with_stdio(false);
	int T;
    cin >>T;
    for(int t = 0; t < T; t++){
        int n;
        cin >> n;
        vector<int> poss;
        vector<int> negs;
        int a;
        for(int i = 0; i < n; i++){
            cin >> a;
            if (a >= 0){
                poss.push_back(a);
            } else {
                negs.push_back(-a);
            }
        }
        sort(poss.begin(), poss.end());
        sort(negs.begin(), negs.end());
        ll ans = 1;
        if (poss.empty()){
            for(int i = 0; i < 5; i++){
                ans *= -1 * negs[i];
            }
            cout << ans << endl;
            continue;
        }
        int i = 0;
        while (i < 5){
            if (i <= 3){
                // consider negative pairs
                if (negs.size() > 1 && (poss.size() < 2 || (negs[negs.size()-1] * negs[negs.size() -2] > poss[poss.size()-1]*poss[poss.size()-2]))) {
                    ans *= negs.back();
                    negs.pop_back();
                    ans *= negs.back();
                    negs.pop_back();
                    i += 2;
                    continue;
                }
            }
            if (!poss.empty()) {
                ans *= poss.back();
                poss.pop_back();
            } else {
                ans *= -1 * negs.back();
                negs.pop_back();
            }
            i += 1;
        }
        cout << ans << endl;
        continue;
    }
	return 0;
}