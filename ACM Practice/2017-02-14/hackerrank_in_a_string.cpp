#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    //basic idea: go through the input string once, and move through "hackerrank" 
    string z = "hackerrank";
    int index = 0; //our index into "hackerrank".  That is, how 'far' into the string have we gotten so far?
    string a;
    int n;
    cin >> n;
    for(int x = 0; x < n; x++){ //for each testcase
        cin >> a;
        index = 0;
        for(int i = 0; i < a.length(); i++){ //i is our index into a, index is our index into 'hackerrank'
            if(index < z.length() && a[i] == z[index]){ //if we haven't seen all of 'hackerrank' yet, and it's a match, move on to the next character
                index++;
            }
        }
        if(index == z.length()){
            cout <<"YES" << endl;
        } else {
            cout <<"NO" << endl;
        }
    }
    return 0;
}
