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
#define ll long long

map<ll, ll> pos;

bool compareVecs(vector<int> lhs, vector<int>rhs){
    return pos[lhs[0]] < pos[rhs[0]];
}

int main(){
    std::ios::sync_with_stdio(false);
    ll n;
    cin >> n;
    vector<ll> xs(n);
    vector<ll> prev(n);
    for(ll i = 0; i < n; i++){
        cin >> xs[i];
        pos[xs[i]] = i;
    }
    set<ll> heads;
    for(ll i = 0; i < n; i++){
        ll val = xs[i];
        set<ll>::iterator best = heads.lower_bound(val);
        if(best == heads.begin()){
            heads.insert(xs[i]);
            prev[i] = -1;
        } else {
            prev[i] = pos[*(--best)];
            heads.erase(best);
            heads.insert(xs[i]);
        }
    }
    vector<vector<int> > seqs;
    for(set<ll>::iterator it = heads.begin(); it != heads.end(); it++){
        int _pos = pos[*it];
        vector<int> seq;
        while(_pos != -1){
            seq.push_back(xs[_pos]);
            _pos = prev[_pos];
        }
        vector<int> qes;
        while(!seq.empty()){
            qes.push_back(seq.back());
            seq.pop_back();
        }
        seqs.push_back(qes);
    }
    sort(seqs.begin(), seqs.end(), compareVecs);
    for(int i = 0; i < seqs.size(); i++){
        for(int j = 0; j < seqs[i].size(); j++){
            cout << seqs[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}