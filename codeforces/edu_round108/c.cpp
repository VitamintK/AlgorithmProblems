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
    for(int t = 0; t < T; t++){
        int n;
        cin >> n;
        vector<int> enroll(n);
        vector<vector<int> > unis(n);
        int u, s;
        for(int i =0; i < n;i++){
            cin >> u;
            u--;
            enroll[i] = u;
        }
        for(int i=0; i<n;i++){
            cin >> s;
            unis[enroll[i]].push_back(s);
        }
        vector<ll> ans(n+1, 0);
        map<int, vector<ll> > pres;
        for(int i = 0; i < n; i++){
            sort(unis[i].rbegin(), unis[i].rend());
            ll pre = 0;
            pres[i].resize(unis[i].size());
            for(int j=0; j<unis[i].size(); j++){
                pre += unis[i][j];
                pres[i][j] = pre;
            }
            for(int k=1;k<=pres[i].size();k++){
                ans[k] += pres[i][k * (pres[i].size()/k) - 1];
            }
        }
        for(int k=1;k<=n;k++){
            cout << ans[k];
            if(k!=n){cout<<" ";}
        }
        cout << endl;
    }
	return 0;
}