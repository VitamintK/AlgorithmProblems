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
    for(int t=0; t<T; t++){
        int n;
        cin >> n;
        string a, b;
        cin >> a;
        cin >> b;
        int diffs = 0;
        vector<int> ones;
        ones.clear();
        for(int i=0; i < n; i++){
            if (a[i] != b[i]){
                diffs++;
            }
            if (a[i] == '1'){
                ones.push_back(i);
            }
        }
        if (!((diffs==n) || (diffs==0))){
            cout << "NO" << endl;
            continue;
        }
        cout << "YES" << endl;
        if (ones.size() == 0){
            if (diffs==0){
                cout << 0 << endl;
            } else {
                cout << 3 << endl;
                cout << "1 1" << endl;
                cout << "2 2" << endl;
                cout << "1 2" << endl;
            }
        } else {
            int flip_parity = (ones.size()+1) % 2; // if 1, then a num opposite a one is flipped
            int k = ones.size();
            bool opposite_is_zero_now = flip_parity ^ (b[ones[0]]=='0');
            if (!opposite_is_zero_now) {
                k+=3;
            }
            cout << k << endl;
            for(int i =0; i < ones.size(); i++){
                cout << ones[i]+1 << " " << ones[i]+1 << endl;
            }
            if (!opposite_is_zero_now) {
                cout << "1 1" << endl;
                cout << "2 2" << endl;
                cout << "1 2" << endl;
            }
        }
    }
	return 0;
}