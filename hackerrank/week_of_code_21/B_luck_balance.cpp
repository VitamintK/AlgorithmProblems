#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N, K;
    cin >> N >> K;
    int L, T;
    long luck = 0;
    vector<int> important;
    for(int i = 0; i < N; i++){
        cin >> L >> T;
        if(T == 0){
            luck += L;
        } else {
            important.push_back(L);
        }
    }
    sort(important.begin(), important.end());
    reverse(important.begin(), important.end());
    for(int i = 0; i < K; i++){
        luck+= important[i];
    }
    for(int i = K; i < important.size(); i ++){
        luck-= important[i];
    }
    cout << luck;
    return 0;
}
