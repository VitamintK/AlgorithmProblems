#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int n;
    int k;
    cin >> n >> k;
    string number;
    cin >> number;
    int used = 0;
    bool changed[100001] = {0};
    for(int i = 0; i < n/2; i++){
        if(number[i] > number[n-1-i]){
            if(used >=k){
                cout << -1 << endl;
                //cout << number[i] << " " << number[n-1-i];
                return 0;
            }
            number[n-1-i] = number[i];
            used++;
            changed[n-1-i] = true;
        } else if(number[n-1-i] > number[i]){
            if(used >=k){
                cout << -1 << endl;
                //cout << i << endl;
                //cout << n-1-i << endl;
                //cout << number[i] << " " << number[n-1-i];

                return 0;
            }
            number[i] = number[n-1-i];
            used++;
            changed[i] = true;
        }
    }
    //cout << number << endl;
    for(int i = 0; i < (n+1)/2; i++){
        if(used >= k){
            break;
        }
        if(number[i] != '9'){
            if(changed[i] || changed[n-1-i]){
                number[i] = '9';
                number[n-1-i] = '9';
                used++;
            } else {
                if(i == n - 1 - i){
                    //cout <<"dfdf" << endl;
                    number[i] = '9';
                    used++;
                } else 
                if(k-used >= 2){
                    number[i] = '9';
                    number[n-1-i] = '9';
                    used+=2;
                }
            }
        }
    }
    cout << number;
    return 0;
}
