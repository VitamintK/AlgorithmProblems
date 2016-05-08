#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int startz[10001] = {0};
int endz[10001] = {0};

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
   
    int notebook[10001];
    int n, d;
    cin >> n >> d;
    int a;
    for(int i = 0; i < n; i++){
        cin >> notebook[i];
        for(int j = 0; j < i; j++){
            if(notebook[i] - notebook[j] == d){
                startz[j]++;
                endz[i]++;
                break;
            }
        }
    }
    long ans;
    for(int i = 0; i < n; i++){
        ans += startz[i] * endz[i];
    }
    cout << ans;
    return 0;
}