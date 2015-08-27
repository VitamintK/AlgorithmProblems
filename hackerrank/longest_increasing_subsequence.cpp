#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//getBestSubsequenceWithTail

int main() {
    int t;
    int n;
    int globalLongest = 0;
    pair<int, int>* subs = new pair<int,int>[t];
    scanf("%d", &t);
    for(int i; i < t; i++){
        scanf("%d", &n);
        pair<int, int> longest = make_pair(1,n);
        for(int j = 0; j<i; j++){
            if(subs[j].second < n && subs[j].first >= longest.first){
                longest = make_pair(subs[j].first + 1, n);
            }
            //cout << longest.first << " " << longest.second << endl;
            //cout << subs[j].first << "--" << subs[j].second << endl;
        }
        subs[i] = longest;
        globalLongest = max(longest.first, globalLongest);
    }
    printf("%d", globalLongest);
    return 0;
}