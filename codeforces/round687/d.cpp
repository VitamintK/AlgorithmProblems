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

// DOESN'T WORK: the actual solution is just to do an n^4 brute force (unless there are 3 numbers with the same MSB, a condition which restricts n to be less than 60)

int main(){
	std::ios::sync_with_stdio(false);
    int n;
    cin >> n;
    vector<ll> nums(n);
    for(int i =0 ; i < n; i++){
        cin >> nums[i];
    }
    int ans = 12345678;
    for(int i = 0; i < n-1; i++){
        ll l = nums[i];
        ll r = nums[i+1];
        int j = i-1;
        while(j >= 0 && (l^nums[j])>l){
            l^=nums[j];
            j--;
        }
        int k = i+2;
        while(r>=l && k<n && (r^nums[k])<r){
            r^=nums[k];
            k++;
        }
        // cout << i << ": " << j << " " << k << endl;
        // cout << "  " << r << " " << l << endl;
        if(r >= l) {
            continue;
        }
        j++;
        k--;
        for(;j<=i;j++){
            while(k>i+1 && (r^nums[k])<l){
                r^=nums[k];
                k--;
            }
            if(r>=l){
                continue;
            }
            // cout << k << "," << j << "," << r << "," << l << endl;
            ans = min(ans, k-j-1);
            l^=nums[j];
        }
    }
    if (ans == 12345678) {
        ans = -1;
    }
    cout << ans << endl;
	return 0;
}