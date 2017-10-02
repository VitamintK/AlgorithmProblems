#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
#define ll long long
bool cust(pair<ll, ll> a, pair<ll, ll> b){
    return a.second > b.second;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    ll n;
    cin >> n;
    vector<pair<ll,ll>> segs;
    ll a;
    for(ll i = 0; i < n; i++){
        cin >> a;
        if(a >= n){
            continue;
        }
        ll start = i+1;
        ll end = i-a;
        start=(start + n+n)%(n);
        end=(end+n+n)%(n);
        //cout << start << " " << end << endl;
        if(end < start){
             segs.push_back(make_pair(start, n-1));
            segs.push_back(make_pair(0,end));
        } else {
            segs.push_back(make_pair(start, end));
        }
    }
    sort(segs.begin(), segs.end());
    for(ll i = 0; i < segs.size(); i++){
        //cout << segs[i].first << " " << segs[i].second << endl;
    }
    priority_queue<pair<ll,ll>, vector<pair<ll,ll>>, decltype(&cust)> pq(cust);
    ll pt = 0;
    ll ans = 0;
    ll ind = 0;
    while(pt < segs.size()){
        ll new_start = segs[pt].first;
        while(pt < segs.size() && segs[pt].first == new_start){
            pq.push(segs[pt]);
            pt++;
        }
        while(pq.top().second < new_start){
            pq.pop();
        }
        if((ll)pq.size() > ans){
           //cout << "index " << new_start << ", amount " << pq.size() << endl;
            ans = (ll)pq.size();
            ind = new_start;
        }
    }
    cout << ind+1 << endl;
    return 0;
}
