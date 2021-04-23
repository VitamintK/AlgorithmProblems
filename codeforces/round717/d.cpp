// TLEs :(((

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

struct data{
    int l;
    int r;
    int nearest_rightmost_neighbor;
    int internal_partitions;
};

vector<vector<data> > tiers;


void get(vector<data> &ans, int l, int r){
    if (l > r){
        return;
    }
    int level = 0;
    int span = 1;
    int n = l;
    while(n%2 == 0 && r+1-l >= span*2){
        level++;
        span *= 2;
        n/=2;
    }
    ans.push_back(tiers[level][n]);
    get(ans, l+span, r);
}

data combine(data l, data r){
    if(l.nearest_rightmost_neighbor > r.r){
        return (data){l.l, r.r, min(l.nearest_rightmost_neighbor, r.nearest_rightmost_neighbor), l.internal_partitions+r.internal_partitions};
    }
    vector<data> d;
    get(d, l.nearest_rightmost_neighbor, r.r);
    data dt = d[0];
    for(int i = 1; i < d.size(); i++){
        dt = combine(dt, d[i]);
    }
    int nearest_rightmost_neighbor = dt.nearest_rightmost_neighbor;
    return (data){l.l, r.r, nearest_rightmost_neighbor, l.internal_partitions+r.internal_partitions+1};
}

int main(){
	std::ios::sync_with_stdio(false);
	int n, q;
	cin >> n >> q;
    vector<int> as(n);
    // vector<map<int, int> > maps(n);
    int lim = 100002;
    vector<int> sieve(lim, 1);
    for(int i = 2; i < lim; i++){
        if (sieve[i] == 1){
            for(int j = i; j<lim; j+=i){
                sieve[j] = i;
            }
        }
    }
    for(int i = 0; i < n; i++){
        cin >> as[i];
        // maps[i][as[i]]++;
    }
    map<int, int> closest_prime_cousin_to_right;
    vector<data> nearest_right_neighbor(n);
    for(int i = n-1; i>=0; i--){
        vector<int> primes;
        int x = as[i];
        int nearest = 912345;
        while(x != 1){
            int p = sieve[x];
            if (closest_prime_cousin_to_right[p] != 0){
                nearest = min(nearest, closest_prime_cousin_to_right[p]);
            }
            primes.push_back(p);
            x /= p;
        }
        for(int j = 0; j < primes.size(); j++){
            closest_prime_cousin_to_right[primes[j]] = i;
        }
        nearest_right_neighbor[i] = (data){i,i,nearest,0};
    }
    tiers.push_back(nearest_right_neighbor);
    while(tiers[tiers.size() - 1].size() > 1){
        auto tier = tiers[tiers.size()-1];
        // vector<map<int, int> > new_tier;
        vector<data> new_tier;
        for(int i = 0; i < tier.size()/2; i++) {
            // map<int, int> new_map;
            // for (auto it = tier[i*2].begin(); it != tier[i*2].end(); it++){
            //     new_map[it->first] += it->second;
            // }
            // for (auto it = tier[i*2+1].begin(); it != tier[i*2+1].end(); it++){
            //     new_map[it->first] += it->second;
            // }
            data new_data = combine(tier[i*2], tier[i*2+1]);
            new_tier.push_back(new_data);
        }
        tiers.push_back(new_tier);
    }
    for(int i = 0; i < q; i++){
        int l, r;
        cin >> l >> r;
        l--;
        r--;
        vector<data> d;
        get(d, l, r);
        data dt = d[0];
        for(int i = 1; i < d.size(); i++){
            dt = combine(dt, d[i]);
        }
        cout << dt.internal_partitions+1 << endl;
    }
	return 0;
}