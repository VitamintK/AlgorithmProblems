#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

int answer(int num){
    //bool negs = false;
    if(num == 1){
        cout << "IMPOSSIBLE" << endl;
        return 0;
    }
    for(double num_of_divisors = 2; (num_of_divisors*(num_of_divisors + 1)/2) < num+2; num_of_divisors ++){
        //if(false){
        if(num/num_of_divisors == ceil(num/num_of_divisors) - (((int)(num_of_divisors + 1)% 2) * 0.5 )){
            cout << num << " = ";
            int skew = (num_of_divisors / 2);
            int i = 0;
            for(; i < num_of_divisors-1; i++){
                //printf( "%f1000.0",  ceil(num/num_of_divisors) + i - skew);
                //printf(" + ");
                //if(ceil(num/num_of_divisors) + i - skew < -1){
                //    negs = true;
                //}
                cout << (int)ceil(num/num_of_divisors) + i - skew << " + ";
            }
            cout << fixed << (int)ceil(num/num_of_divisors) + i - skew << endl;
            return 0; 
        }
    }
    cout << "IMPOSSIBLE" << endl;
    return 0;
}

int main() {
    cout.setf(ios::fixed);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int T;
    cin >> T;
    int num;
    for(int i= 0; i<T; i++){
        cin >> num;
        answer(num);
    }
    //for(num =0; num<100000; num++){
    //    if(answer(num)){
    //        cout << num;
    //    }
    //}
    return 0;
}
