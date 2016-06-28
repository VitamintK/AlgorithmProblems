#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
#define ll long long

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    //create factorial table
    ll facts[19];
    facts[0] = 1;
    for(int i = 1; i <= 18; i++){
        facts[i] = facts[i-1] * (i);
    }
    //read in the numbers and record the amount of times each number appears in the sequence
    map<int, int> nums;
    int N;
    cin >> N;
    int num;
    for(int i = 0; i < N; i++){
        cin >> num;
        nums[num]++;
    }
    //calculate the answer
    double ans = (double)facts[N];
    for(const auto &nnn : nums){
        ans/= (double)(facts[nnn.second]);
    }
    cout.precision(6);
    cout << fixed << ans;
    return 0;
}
