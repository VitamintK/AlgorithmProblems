#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
//ios::sync_with_stdio(false);

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int T;
    int n;
    //long long a;
    long long as[107];
    bool seen_one;
    int new_n;
    int n_offset = 0;
    cin >> T;
    for(int t = 0; t < T; t++){
        cin >> n;
    n_offset = 0;
    seen_one = false;
    new_n = n;
    for(int i = 0; i < n; i++){
        cin >> as[i];
    }
        if(n == 1){
            if(as[0] == 1){
                cout << 2 << endl;
                cout << "1 0" << endl;
            } else {
            cout << n+2 << endl;
            cout << 1 << " " << 1 << " " << as[0] -1 << endl;
            }
            continue;
            
        }if(n == 2){
            if(as[0] == 1){
                cout << 2 << endl;
                cout << 1 << as[1] + 1;
            } else {
                cout << 3 << endl;
                cout << 1 << " " << as[1]+1 << " " << as[0]-1 << endl;}
            continue;
        } else {
            new_n = new_n + 2;
            int pert_zero;
            if(n%2 == 0){
                //new_n = new_n - 1;
                pert_zero = n-3;
                as[pert_zero+2]++;
                as[pert_zero] = as[pert_zero] - 1;
                if(as[pert_zero] == 0){new_n = new_n - 2;as[pert_zero] = -1;}
                as[pert_zero+3] = as[pert_zero+1] - 1;
                as[pert_zero+1] = 1;
            } else {
                pert_zero = n-2;
                as[pert_zero+2] = 1;
                as[pert_zero] = as[pert_zero] - 1;
                if(as[pert_zero] == 0){new_n = new_n ; n_offset = -2; as[pert_zero] = -1;}
                as[pert_zero+3] = as[pert_zero+1] - 1;
                as[pert_zero+1] = 1;
            }
            
            //as[pert_zero+2]++;
        }
    
        // for(int i =0; i < n+1; i++){
        //     if(as[i+1] == 0){
        //         as[i] = as[i] + as[i+2];
        //         as[i+2] = -1;
        //         as[i+1] = -1;
        //         new_n-=2;
        //     }
        // }
        // if(as[i+3]) 

    cout << new_n << endl;
    for(int i = 0; i < new_n; i++){
        if(as[i+1] != -1){
            cout << as[i] << " ";
        } else {
            cout << as[i] + as[i+2] << " ";
            i++;i++;
        }
    }
    cout << endl;    
    
    }
    return 0;
}
