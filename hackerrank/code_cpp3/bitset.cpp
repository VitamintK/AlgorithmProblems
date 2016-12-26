#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int N;
    int S;
    int P;
    int Q;
    int a;
    bitset<2147483648>* bs = new bitset<2147483648>();
    cin >> N >> S >> P >> Q;
    //cout << N << S << P << Q;
    a = S % 2147483648;
    //Q = Q% 2147483648;
    for (int i = 1; i <  N; i++){
        bs->set(a);
        //cout << a << endl;
        a = (a*P + Q)&((1 << 31) - 1);
    }
    bs->set(a);
    cout << bs->count();
    return 0;
}
