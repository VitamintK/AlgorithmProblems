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
    for(int t=0; t < T; t++){
        int n;
        cin >> n;
        vector<int> as(n);
        for(int i=0; i < n; i++){
            cin >> as[i];
        }
        vector<int> is_last(n, 0);
        set<int> seen;
        for(int i = n-1; i >= 0; i--){
            if(seen.find(as[i]) == seen.end()){
                seen.insert(as[i]);
                is_last[i] = 1;
            }
        }

        set<int> used;
        set<pair<int, int>> minbst;
        set<pair<int, int>> maxbst;
        vector<int> ans;
        int parity = 1;
        int j = -1;
        for(int i = 0; i < n; i++){
            if(used.find(as[i]) == used.end()){
                minbst.insert({as[i], i});
                maxbst.insert({-as[i], i});

                if(is_last[i]){
                    while (j < i){
                        int idx, v;
                        if (parity == -1){
                            if (minbst.size() == 0){
                                break;
                            }
                            auto it = minbst.begin();
                            idx = it->second;
                            v = it -> first;
                            minbst.erase(it);
                        } else {
                            if (maxbst.size() == 0){
                                break;
                            }
                            auto it = maxbst.begin();
                            idx = it->second;
                            v = -(it -> first);
                            maxbst.erase(it);
                        }
                        if ((idx > j) && (used.count(v)==0)){
                            ans.push_back(v);
                            used.insert(v);
                            parity *= -1;
                            j = idx;
                            if (v == as[i]){
                                break;
                            }
                        }
                    }
                }
            }
        }
        cout << ans.size() << endl;
        for(int i=0; i < ans.size(); i++){
            cout << ans[i] << " ";
        }
        cout << endl;
    }
    
	return 0;
}