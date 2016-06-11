#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int W, B, P;
    cin >> W >> B >> P;
    int a;
    long long whouses[16][10];
    long long combos[65536][10];
    fill((long long*)combos, (long long*)combos+655360,0ll);
    for(int i = 0; i < W; i++){
        for(int j = 0; j < P; j++){
            cin >> whouses[i][j];
        }
    }
    for(int i = 0; i < pow(2, W); i++){
        for(int pos = 0; pos < W; pos++){
            if((i>>pos)&1 == 1){
                for(int j = 0; j < P; j++){
                    combos[i][j]+=whouses[pos][j];
                }
            }
        }
    }
    int one_bits = -1;
    long long order[10];
    bool flag;
    for(int i = 0; i < B; i++){
        one_bits = 17;
        for(int j = 0; j < P; j++){
            cin >> order[j];
        }
        for(int combo = 0; combo < pow(2, W); combo++){
            flag = true;
            for(int p = 0; p < P; p++){
                if(combos[combo][p] < order[p]){
                    flag = false;
                    break;
                }
            }
            if(flag){
                int bits = 0;
                for(int place = 0; place < W; place++){
                    bits+=((combo>>place)&1);
                }
                one_bits = min(bits, one_bits);
            }
        }
        if(one_bits == 17){
            cout << -1 << endl;
        } else {
        cout << one_bits << endl;
        }
    }
    return 0;
}
