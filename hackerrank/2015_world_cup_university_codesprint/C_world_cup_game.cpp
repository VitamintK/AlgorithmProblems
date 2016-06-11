#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define ll long long

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    ll nodes[500001] = {0};
    ll parent[500001] = {0};
    vector<ll> children[500001];
    ll N;
    cin >> N;
    for(ll i = 1; i <= N; i++){
        cin >> nodes[i];
    }
    ll a, b;
    ll root;
    for(ll i = 0; i < N-1; i++){
        cin >> a >> b;
        if (parent[a] != 0){
            parent[b] = a;
            children[a].push_back(b);
        } else if(parent[b] != 0){
            parent[a] = b;
            children[b].push_back(a);
        } else {
            parent[a] = a;
            parent[b] = a;
            root = a;
            children[a].push_back(b);
        }
    }
    
    vector<ll> stack;
    stack.push_back(root);
    ll look;
    while(!stack.empty()){
        look = stack.back();
        stack.pop_back();
        if(look < 0){
            if(root != -look){
                nodes[parent[-look]]+=nodes[-look];
            }
        } else {
            stack.push_back(-look);
            for(ll i : children[look]){
                stack.push_back(i);
            }
        }
    }
    ll best = 0;
    for(ll i = 1; i <= N; i++){
        ll worst = 1e18;
        for(ll child : children[i]){
            if(nodes[root] - nodes[child] < worst){
                worst = nodes[root] - nodes[child];
            }
        }
        if(i != root && nodes[i] < worst){
            worst = nodes[i];
        }
        if(worst > best){
            best = worst;
        }
    }
    cout << best;
    return 0;
}
