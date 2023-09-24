// ok I think I can do this with a segtree segment tree but not sure if I can do it otherwise
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

vector<ll> endpoints;
vector<ll> t(1100000 * 4, 0);
vector<ll> ls(1100000 * 4, 0);
vector<ll> rs(1100000 * 4, 0); // always exclusive

void increment(ll l, ll r, int root, ll amount) {
    if (l <= ls[root] && rs[root] <= r) {
        t[root] += amount;
    } else if (l < rs[root] && ls[root] < r) {
        increment(l, r, root*2, amount);
        increment(l, r, root*2+1, amount);
    }
}

void build(int root, int l, int r){
	// if(root >= n){
	// 	return;
	// }
    if (r-l > 1) {
        int mid = (l+r)/2;
        build(root*2, l, mid);
        build(root*2+1, mid, r);
    }
	ls[root] = endpoints[l];
    rs[root] = endpoints[r];
}

ll query(ll l, ll r, int root) {
    if (l <= ls[root] && rs[root] <= r) {
        return t[root];
    } else if (l < rs[root] && ls[root] < r) {
        return query(l, r, root*2) + query(l, r, root*2+1);
    } else {
        return 0;
    }
}


int main(){
	std::ios::sync_with_stdio(false);
	ll n, m, k;
	cin >> n >> m >> k;
    vector<pair<ll, int>> xs(n+2);
    for (int i =0; i < n; i++){
        ll x;
        cin >> x;
        xs[i+1] = make_pair(x, -i);
    }
    sort(xs.begin(), xs.end());
    set<ll> added;
    added.insert(0);
    endpoints.push_back(0);
    added.insert(m+1);
    endpoints.push_back(m+1);
    for(int i=0; i < n; i++){
        if (added.count(xs[i].first - 1)==0) {
            endpoints.push_back(xs[i].first - 1);
            added.insert(xs[i].first - 1);
        }
        if(added.count(xs[i].first)==0) {
            endpoints.push_back(xs[i].first);
            added.insert(xs[i].first);
        }
        if (added.count(xs[i].first + 1)==0) {
            endpoints.push_back(xs[i].first + 1);
            added.insert(xs[i].first + 1);
        }
    }
    build(1, 0, endpoints.size()-1);

    ll prev_endpoint = 0;
    for (int i =0 ; i < n; i++){
        int r_endpoint = i+k+1;
        int r_endpoint_value = xs[r_endpoint].first;
        increment()
    }


	return 0;
}