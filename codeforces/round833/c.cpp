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
    for (int t=0; t<T; t++){
        int n;
        cin >> n;
        vector<ll> as(n);
        vector<int> zero_indices;
        int num_zeroes_before_zero = 0;
        ll run = 0;
        for(int i=0; i<n; i++){
            cin >> as[i];
            if(as[i]==0){
                zero_indices.push_back(i);
            }
            run += as[i];
            if (zero_indices.size() == 0 && run==0){
                num_zeroes_before_zero++;
            }
        }
        int ans = 0;
        for(int i=0; i<zero_indices.size(); i++){
            int l = zero_indices[i];
            int r;
            if(i < zero_indices.size()-1){
                r = zero_indices[i+1];
            } else {
                r = n;
            }
            map<ll, int> counter;
            ll run = 0;
            int best = 0;
            for(int j=l; j<r; j++){
                run += as[j];
                counter[run]++;
                best = max(best, counter[run]);
            }
            ans += best;
        }
        cout << ans+num_zeroes_before_zero << endl;
    }
	return 0;
}