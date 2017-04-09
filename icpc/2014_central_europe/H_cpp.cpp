#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int microwave[10][2] = {{3,1},{0,0},{0,1},{0,2},{1,0},{1,1},{1,2},{2,0},{2,1},{2,2}};

bool microwave_safe(int time){
    if(time < 1 || time > 999){
        return false;
    }
    int oldnum=time%10;
    int newnum;
    time = time/10;
    while(time > 0){
        newnum= time%10;
        time = time /10;
        if(!(microwave[newnum][0] <= microwave[oldnum][0] && microwave[newnum][1] <= microwave[oldnum][1])){
            return false;
        }
        oldnum = newnum;
    }
    return true;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N;
    cin >> N;
    int target_time;
    for(int i = 0; i<N; i++){
        cin >> target_time;
        int offset = -1;
        bool positive = false;
        bool negative = false;
        while(positive == false && negative == false){
            offset++;
            positive = microwave_safe(target_time + offset);
            negative = microwave_safe(target_time - offset);
        }
        if(positive && negative){
            cout << target_time + offset << " " << target_time - offset << endl;
        }
        else if(positive){
            cout << target_time + offset << endl;
        } else {
            cout << target_time - offset << endl;
        }
    }
    return 0;
}
