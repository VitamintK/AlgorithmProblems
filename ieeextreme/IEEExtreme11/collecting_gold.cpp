#include <iostream>
#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<ll> values(n);
    vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53}
;
    vector<ll> sum_of_primes;
    sum_of_primes.push_back(2);
    for(int i = 1; i < 16; i++){
        sum_of_primes.push_back(sum_of_primes[i-1]*primes[i]);
        //cout << sum_of_primes[i] << endl;
    }
   // for(int i = 0; i < 12; i++){
    //    cout << sum_of_primes[i] << endl;
    //}
    map<ll, ll> id_to_index;
    ll min_value = 1234567890123456789LL;
    ll max_value = 0;
    for(ll i = 0; i < n; i++){
        cin >> values[i];
        min_value = min(min_value, values[i]);
        max_value = max(max_value, values[i]);
        id_to_index[values[i]] = i;
        ll j = 0;
        while(sum_of_primes[j+1] <= values[i]){
            j++;
        }
        values[i] = j+1;
    }
    vector<vector<pair<ll,ll>> > edges(n);
    for(ll i = 0; i < m; i++){
        ll u, v, d;
        cin >> u >> v >> d;
        edges[id_to_index[u]].push_back(make_pair(-d, id_to_index[v]));
        edges[id_to_index[v]].push_back(make_pair(-d, id_to_index[u]));
    }
    priority_queue<pair<ll, pair<ll, ll> > > pq; //-cost, (gold collected, id)
    pq.push(make_pair(0, make_pair(values[id_to_index[min_value]], id_to_index[min_value])));
    map<ll, ll> visited;
    while(!pq.empty()){
        pair<ll, pair<ll, ll>> ex = pq.top();
        ll cost = ex.first;
        ll gold = ex.second.first;
        ll id = ex.second.second;
        //cout << id << " : " << gold << endl;
        pq.pop();
        if(visited.count(id) > 0 && visited[id] < gold){
            continue;
        }
        visited[id] = gold;
        if(id == id_to_index[max_value]){
            cout << gold << endl;
            return 0;
        }
        for(ll i = 0; i < edges[id].size(); i++){
            pair<ll, ll> neighbor = edges[id][i];
            if(visited.count(neighbor.second) < 1 || visited[neighbor.second] <= gold+values[neighbor.second]){
                pq.push(make_pair(cost + neighbor.first, make_pair(gold + values[neighbor.second], neighbor.second)));
            }
        }
    }
    return 0;
}