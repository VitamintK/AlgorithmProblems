#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
using namespace std;

#define ull unsigned long long
#define ll unsigned long long



int main(){
    std::ios::sync_with_stdio(false);
    ll n, k;
    cin >> n >> k;
    //binary search for the number of nests we'll need
    ll lo = 0;
    ll hi = k;
    while(hi >= lo){
        ll mid = lo + (hi-lo)/2;
        if((mid*(mid+1))/2 > k){
            hi = mid-1;
        } else {
            lo = mid+1;
        }
    }
    ll nests = lo-1;
    ll adtl = k - (nests*(nests+1))/2;
    nests++;
    //cout << nests << " " << adtl << endl;
    int need_2 = (adtl==0 ? 0 : 1);
    if (nests + need_2 > n){
        cout << "Impossible" << endl;
        return 0;
    }
    ll stack = 0;
    for(ll i = 0; i < nests; i++){
        cout << "(";
        stack++;
        if(stack == adtl){
            cout << "()";
        }
    }
    for(ll i = 0; i < nests; i++){
        cout << ")";
        stack--;
    }

    ll p_extra = n - nests - need_2;
    for(ll i = 0; i < p_extra; i++){
        cout << "()";
    }
    cout << endl;
    return 0;
}   