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
        // ans.push_back(as[i]);
        // ans.push_back(as[start2+i]);
        cout << as[i] << " ";
        if(start2+i < n) {
            cout << as[start2+i] << " ";
        }
    }
    cout << endl;
	return 0;
}