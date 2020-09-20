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
    int n;
    cin >> n;
    vector<int> as(n);
    for(int i = 0; i < n; i++) {
        cin >> as[i];
    }
    struct {
        bool operator()(int a, int b) const
        {   
            return a > b;
        }   
    } customLess;
    sort(as.begin(), as.end(), customLess);
    vector<int> ans;
    int start2 = (n+1)/2;
    for(int i =0; i < start2; i++) {
        ans.push_back(as[i]);
        if (start2+i < n) {
            ans.push_back(as[start2+i]);
        }
        // cout << as[i] << " ";
        // if(start2+i < n) {
        //     cout << as[start2+i] << " ";
        // }
    }
    // int mid_elem = ans[n/2];
    // if()
    int first_repeat = -1;
    for(int i = 0; i < n-1; i++) {
        if (ans[i] == ans[i+1]) {
            first_repeat = i+1;
            break;
        }
    }
    if (first_repeat != -1 && ans[n-1] < ans[first_repeat]) {
        rotate(ans.begin()+(first_repeat), --ans.end(), ans.end());
    }

    int tot = 0;
    for(int i = 1; i < n-1; i++) {
        if (ans[i] < ans[i-1] && ans[i] < ans[i+1]) {
            tot++;
        }
    }
    cout << tot << endl;
    for(int i = 0; i < n; i++){
        cout << ans[i] << " ";
    }
    cout << endl;
	return 0;
}