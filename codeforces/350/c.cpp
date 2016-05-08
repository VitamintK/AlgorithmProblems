#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <signal.h>
#include <unordered_map>
using namespace std;
//ios::sync_with_stdio(false);
long long n, k;

unordered_map<long long, long> langs;
long long bs[200001];
long long cs[200001];
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    long n, m;
    cin >> n;
    long long a;
    for(long i = 0; i < n; i++){
        cin >> a;
        langs[a]++;
    }
    cin >> m;
    for(long i = 0; i< m; i++){
        cin >> bs[i];
    }
    for(long i = 0; i<m; i++){
        cin >> cs[i];
    }
    int best_index = 0;
    int best_b = langs[bs[0]];
    int best_c = langs[cs[0]];

    for(long i = 0; i < m; i++){
        if(langs[bs[i]] > best_b){
            best_index = i;
            best_b = langs[bs[i]];
            best_c = langs[cs[i]];
        } else if(langs[bs[i]] == best_b && langs[cs[i]] > best_c){
            best_index = i;
            best_c = langs[cs[i]];
        }
    }
    cout << best_index+1;


    return 0;
}
