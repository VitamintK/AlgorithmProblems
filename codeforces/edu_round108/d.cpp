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

vector<ll> as;
vector<ll> bs;

vector<vector<ll> > cache;
vector<vector<bool> > cached;

ll swap_gain(int l, int r){
    if (cached[l][r]){
        return cache[l][r];
    }
    if (l>=r){
        return 0; 
    }
    ll prevswapgain = swap_gain(l+1, r-1);
    ll ans = prevswapgain + as[r]*bs[l] + as[l]*bs[r] - as[l]*bs[l] - as[r]*bs[r];
    cached[l][r] = true;
    cache[l][r] = ans;
    // cout << l << " " << r << " " << ans << endl;
    return ans;
}

int main(){
	std::ios::sync_with_stdio(false);
	int n;
    cin >> n;
    as.resize(n);
    bs.resize(n);
    for(int i=0; i <n;i++){
        cache.push_back(vector<ll>(n,-1));
        cached.push_back(vector<bool>(n,false));
    }
    for(int i =0;i<n;i++){
        cin >> as[i];
    }
    for(int i=0;i<n;i++){
        cin >> bs[i];
    }
    ll baseline = 0;
    for(int i =0;i<n;i++){
        baseline += (ll)as[i]* (ll)bs[i];
    }
    ll ans = 0;
    for(int i =0; i < n; i++){
        for(int j = i; j<n;j++){
            ans = max(ans, swap_gain(i,j));
        }
    }
    cout << baseline+ans << endl;
	return 0;
}