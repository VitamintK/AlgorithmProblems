#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;

bool custcomp(pair<long long, long long> lhs, pair<long long, long long> rhs){
    return (lhs.second > rhs.second) || (lhs.second == rhs.second && lhs.first > rhs.first);
}

int main() {
    ios::sync_with_stdio(false);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    long long N;
    cin >> N;
    long long P, T;
    int type;
    queue<pair<long long, long long> > recent;
    multiset<pair<long long, long long>, bool(*)(pair<long long, long long>, pair<long long, long long>)> largest(custcomp);
    for(long long i = 0; i < N; i++){
        cin >> type;
        if(type == 1){
            cin >> P >> T;
            recent.push(make_pair(T, P));
            largest.insert(make_pair(T,P));
        } else {
            cin >> T;
            while(!recent.empty() && recent.front().first <= T-60){
                //cout << " 1" << endl;
                largest.erase(recent.front());
                //cout << "1.5" << endl;
                recent.pop();
                //cout << "2" << endl;
            }
            if(largest.empty()){
                cout << -1 << endl;
            } else {
                cout << largest.begin()->second << endl;
            }
        }
    }
    return 0;
}
