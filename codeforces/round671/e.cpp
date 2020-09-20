#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <utility>
#include <iomanip>
#include <cmath>

#define ll long long
#define ull unsigned long long
using namespace std;

ll MOD = 1000000007;

// upsolved after contest

vector<pair<ll, int>> prime_factorize(ll n) {
    vector<pair<ll, int>> factorization;
    ll x = n;
    for(ll i =2; i*i <= n; i++){
        if (x%i == 0){
            int cnt = 0;
            while(x%i == 0){
                cnt++;
                x/=i;
            }
            factorization.push_back(make_pair(i, cnt));
        }
    }
    if (x > 1) {
        factorization.push_back(make_pair(x, 1));
    }
    return factorization;
}

set<ll> get_divisors(ll n) {
    set<ll> divisors;
    for(ll i =2; i*i <= n; i++){
        if(n%i == 0){
            divisors.insert(i);
            divisors.insert(n/i);
        }
    }
    divisors.insert(n);
    return divisors;
}

int main(){
	std::ios::sync_with_stdio(false);
    vector<int> sieve(40000, -1);
    vector<int> primes;
    // for(int i = 2; i < sieve.size(); i++ ){
    //     if(sieve[i] == -1) {
    //         for(int j = i*2; j<sieve.size(); j+=i) {
    //             sieve[j] = i;
    //         }
    //         primes.push_back(i);
    //     }
    // }
	int T;
    cin >>T;
    for(int t = 0; t < T; t++){
        int n;
        cin >> n;
        vector<pair<ll, int> > prime_factors = prime_factorize(n);
        // if(prime_factors.size() == 2 && prime_factors[0].second == 1 && prime_factors[1].second == 1){
        //     cout << prime_factors[0].first << " " << prime_factors[1].first << " " << n << endl;
        //     cout << 1 << endl;
        //     continue;
        // }
        set<ll> divisors = get_divisors(n);
        vector<ll> ans(0);
        vector<ll> use_after(prime_factors.size(), 0);
        for(int i = 0; i < prime_factors.size(); i++){
            for(auto it = divisors.begin(); it!=divisors.end();){
                if (*it==prime_factors[i].first) {
                    it = divisors.erase(it);
                    continue;
                }
                if (*it%prime_factors[i].first==0 && *it%prime_factors[(i+1)%prime_factors.size()].first==0){
                    use_after[i] = *it;
                    it = divisors.erase(it);
                    break;
                } else {
                    it++;
                }
            }
        }
        int count=0;
        for(int i =0; i<prime_factors.size();i++){
            if(i != 0) {
                cout << " ";
            }
            cout << prime_factors[i].first;
            for(auto it = divisors.begin(); it!=divisors.end();){
                if(*it%prime_factors[i].first==0){
                    cout << " " << *it;
                    it = divisors.erase(it);
                } else {
                    it++;
                }
            }
            if(use_after[i] != 0){
                cout << " " << use_after[i];
            } else {
                count++;
            }
        }
        cout << endl << count << endl;
    }
	return 0;
}