#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
//https://www.hackerrank.com/challenges/bear-and-steady-gene
bool wegood(int minimum[], int real[]){
    //each of the real (actual) character counts is at least the minimum character count
    for(int i = 0; i < 4; i++){
        if(real[i] < minimum[i]){
            return false;
        }
    }
    return true;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    long n;
    string k;
    cin >> n;
    cin >> k;
    map<char, int> dict;
    dict['A'] = 0;
    dict['C'] = 1;
    dict['G'] = 2;
    dict['T'] = 3;
    int ps[4] = {0};
    for(int i = 0; i < k.length(); i++){
        ps[dict[k[i]]]++;
    }
    int thesum = ps[0] + ps[1] + ps[2] + ps[3];
    for(int i = 0 ; i < 4; i++){
        ps[i] = max(ps[i] - (thesum/4), 0);
    }
    int counts[4] = {0};
    int left = 0; //inclusive
    int right = 0; //exclusive
    int bestans = 1000000;
    if(wegood(ps, counts)){
        cout << 0;
        return 0;
    }
    while(!wegood(ps, counts) && right < k.length()){
        //while we don't yet have the minimal set of chars to replace, increment the right pointer
        counts[dict[k[right]]]++;
        right++;
        while(wegood(ps, counts)){
            //while we already do have the minimal set of chars to replace, increment the left pointer
            bestans = min(bestans, right-left);
            //since we have a suitable candidate answer: if it is less than the previous best candidate, it is the new best.
            counts[dict[k[left]]]--;
            left++;
        }
    }
    cout << bestans;
    return 0;
}
