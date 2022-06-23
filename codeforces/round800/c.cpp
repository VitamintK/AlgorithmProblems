// g++ -std=c++17 x.cpp && ./a.out
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
	int T;
    cin >> T;
    for (int t = 0; t < T; t++){
        int n;
        cin >> n;
        vector<ll> arr(n);
        arr.resize(n);
        ll count = 0;
        int last_nonzero = -1;
        for(int i = 0; i < n; i++){
            cin >> arr[i];
            count += arr[i];
            if (arr[i] != 0){
                last_nonzero = i;
            }
        }
        if (last_nonzero == -1) {
            cout << "Yes" << endl;
            continue;
        }
        if (count != 0) {
            cout << "No" << endl;
            continue;
        }
        arr[0]--;
        arr[last_nonzero]++;
        int pass = 1;
        for(int i = 0; i < n; i++){
            count += arr[i];
            if (count < 0){
                pass = 0;
            }
        }
        if (pass==1){
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
    
	return 0;
}