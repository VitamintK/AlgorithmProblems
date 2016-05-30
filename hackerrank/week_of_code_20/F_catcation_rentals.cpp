//THIS WILL BE O(N*K), which, when n and k are both 10^5 (their max size), will take too long.  oh well (shrug)

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct node{
    bool alloc = false;
    int low;
    int high;
    int max_high;
};

int parent(int i){
    return i/2;
}
int lc(int i){
    return (i*2);
}
int rc(int i){
    return (i*2)+1;
}

node tree[100001];

void insert(int node, int low, int high){
    if(!tree[node].alloc){
        tree[node].low = low;
        tree[node].high = high;
        tree[node].max_high = high;
        tree[node].alloc = true;
    }
    if(tree[node].low == low){
        tree[node].high = max(tree[node].high, high);
    } else if(tree[node].low < low){
        tree[node].max_high = max(tree[node].high, high);
        insert(lc(node), low, high);
    } else{
        tree[node].max_high = max(tree[node].high, high);
        insert(rc(node), low, high);
    }
}


bool overlap(int roooot, int low, int high){
    if(!tree[roooot].alloc){
        return false;
    }
    if(tree[roooot].low <= high && low <= tree[roooot].high ){
        return true;
    }
    if(tree[lc(roooot)].max_high >= low){
        return overlap(lc(roooot), low, high);
    } else if(tree[rc(roooot)].low < high){
        return overlap(rc(roooot), low, high);
    }
    return false;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, D, k;
    cin >> n >> D >> k;
    int a, b;
    pair<int, int> inputs[100001];
    for(int i = 0; i < n; i++){
        cin >> a >> b;
        inputs[i] = make_pair(a, b);
    }
    int d;
    long ans;
    for(int j = 0; j < k; j++){
        cin >> d;
        fill(tree, tree+100001, node{});
        ans = 0;
        for(int i = 0; i < n; i++){
            if((1+inputs[i].second-inputs[i].first >= d) && (!overlap(1,inputs[i].first, inputs[i].second))){
                ans+=(1+inputs[i].second-inputs[i].first);
                insert(1,inputs[i].first, inputs[i].second);
            }
        }
        cout << ans << endl;
    }
    return 0;
}
