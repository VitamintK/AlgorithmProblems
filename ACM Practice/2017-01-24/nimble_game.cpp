//Written by Linh Chu
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++){
        int result = 0;
        int N;
        cin >> N;
        for (int i = 0; i < N; i++){
            int temp;
            cin >> temp;
            result ^= (temp%2) * i;
        }
        cout << (result > 0 ? "First" : "Second") << '\n';
    }
    return 0;
}
