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

//map<ll, ll> pos;

bool compareVecs(vector<int> lhs, vector<int>rhs){
     return lhs[lhs.size()-1] < rhs[rhs.size()-1];
}

int main(){
    std::ios::sync_with_stdio(false);
    ll n;
    cin >> n;
    vector<ll> xs(n);
    //vector<ll> prev(n);
    for(ll i = 0; i < n; i++){
        cin >> xs[i];
        //pos[xs[i]] = i;
    }
    set<vector<ll>> heads;
    for(ll i = 0; i < n; i++){
        ll val = xs[i];
        auto best = lower_bound(heads.begin(), heads.end(), val, compareVecs);
        if(best == heads.begin()){
            vector<ll> hah;
            hah.push_back(xs[i]);
            heads.insert(hah);
            //prev[i] = -1;
        } else {
            //prev[i] = pos[*(--best)];
            //heads.erase(best);
            (*best).push_back(xs[i]);
        }
    }
    // vector<vector<int> > seqs;
    // for(set<ll>::iterator it = heads.begin(); it != heads.end(); it++){
    //     int _pos = pos[*it];
    //     vector<int> seq;
    //     while(_pos != -1){
    //         seq.push_back(xs[_pos]);
    //         _pos = prev[_pos];
    //     }
    //     vector<int> qes;
    //     while(!seq.empty()){
    //         qes.push_back(seq.back());
    //         seq.pop_back();
    //     }
    //     seqs.push_back(qes);
    // }
    //sort(seqs.begin(), seqs.end(), compareVecs);
    for(auto it = heads.begin(); it != heads.end(); i++){
        for(int j = 0; j < it->size(); j++){
            cout << *it[j] << " ";
        }
        cout << endl;
    }

    return 0;
}   