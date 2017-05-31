//https://www.hackerrank.com/challenges/palindrome-index
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    string s;
    for(int i = 0; i < n; i++){
        cin >> s;
        bool foundasoln = false;
        for(int j = 0; j < (s.length()+1)/2; j ++){
            bool didntwork = false;
            if(s[j] != s[s.length() - j - 1]){
                string test;
                //try deleting s[j]
                test = string(s);
                test.erase(j, 1);
                for(int k = 0; k < (test.length()+1)/2; k++){
                    if(test[k] != test[test.length() - k -1]){
                        didntwork = true;
                        break;
                    }
                }
                if(didntwork == false){
                    cout << j << endl;
                    foundasoln = true;
                    break;
                }
                //try deleting s[s.length - j - 1]
                didntwork = false;
                test = string(s);
                test.erase(test.length()-j-1, 1);
                for(int k = 0; k < (test.length()+1)/2; k++){
                    if(test[k] != test[test.length() - k -1]){
                        didntwork = true;
                        break;
                    }
                }
                if(didntwork == false){
                    cout << s.length()-j-1 << endl;
                    foundasoln = true;
                    break;
                }
            }
        }
        if(foundasoln == false){
            cout << "-1" << endl;
        }
    }
    return 0;
}
