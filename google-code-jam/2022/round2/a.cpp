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
    for(int t=0; t<T;t++) {
        int n, k;
        cin >> n >> k;
        if((k%2==1) || (k<n-1)) {
            cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
            continue;
        }
        vector<pair<int, int>> moves;
        int shortcuts = 0;
        int x = 0;
        int path = n-1;
        for(int i = n; i >0; i--){
            // cout << "i: " << i << endl;
            for (int j= 0; j < 2; j++){
                if (i==n){j=1;}
                int extend = (i/2) * 2;
                if (extend + path > k) {
                    int take = (k-path)/2;
                    path += take * 2;
                    x += (i+1)/2 + take;
                    for(int k = 0; k < extend/2 - take; k++) {
                        shortcuts++;
                        // cout << i << endl;
                        if (j==0){
                            moves.push_back(make_pair(x, x +(i-1)*4 +1));
                            x += (i-1)*4 + 1;
                            i -= 2;
                        } else {
                            moves.push_back(make_pair(x, x +(i-1)*2 + (i-2)*2 +1));
                            x += (i-1)*2 + (i-2)*2 + 1;
                            i-=2;
                        }
                    }
                    // i--;
                } else {
                    path += extend;
                    x += i;
                }
            }
        }
        cout << "Case #" << t+1 << ": " << shortcuts << endl;
        for(int i =0 ; i < shortcuts; i++){
            cout << moves[i].first << " " << moves[i].second << endl;
        }
    }
    
	return 0;
}