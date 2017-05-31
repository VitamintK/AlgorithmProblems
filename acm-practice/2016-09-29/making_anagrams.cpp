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

//https://www.hackerrank.com/challenges/ctci-making-anagrams

using namespace std;

int number_needed(string a, string b) {
   return 0;
}

int main(){
    string a;
    cin >> a;
    string b;
    cin >> b;
    int as[26] = {0};
    int bs[26] = {0};
    for(int i = 0; i < a.length(); i++){
        as[a[i] - 97]++;
    }
    
    for(int i = 0; i < b.length(); i++){
        bs[b[i] - 97]++;
    }
    int n = 0;
    for(int i = 0; i < 26; i++){
        n+= abs(bs[i] - as[i]);
    }
    cout << n << endl;
    return 0;
}
