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
        int x;
        cin >> n >> x;
        vector<int> as(n);
        ll dist_to_x = 0;
        bool any_diff_from_x = false;
        bool any_same_as_x = false;
        for(int i = 0; i < n; i++){
            cin >> as[i];
            if (as[i] != x) {
                any_diff_from_x = true;
            } else {
                any_same_as_x = true;
            }
            dist_to_x += x-as[i];
        }
        if (any_diff_from_x == false) {
            cout << 0 << endl;
        } else if(any_same_as_x == true || dist_to_x == 0) {
            cout << 1 << endl;
        } else {
            cout << 2 << endl;
        }
    }
	return 0;
}