//I'm guessing they were looking for linear preprocessing and constant querying but i thought it would be fun and easy
//  to just put everything in a set and fancily use set binary search tricks to get queries in log(n).
//  (although I didn't check edge cases that I think might break this, like if b is less than 2 or if a is greater than the biggest
//  prime maybe?  it passed all the system tests though!)
#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    set<int> primes;
    vector<int> sieve(1000001);
    for(int i = 2; i < 1000001; i++){
        if(sieve[i] == 0){
            primes.insert(i);
            sieve[i] = 1;
            for(int j = i*2; j < 1000001; j+=i){
                sieve[j] = 1;
            }
        }
    }
    int q;
    cin >> q;
    for(int i = 0; i < q; i++){
        int a, b;
        cin >> a >> b;
        //cout << *(--primes.upper_bound(b)) - *(--primes.upper_bound(a)) << endl;
        //cout << *(--primes.upper_bound(b)) << " " << *(--primes.upper_bound(a)) << endl;
        cout << max(0, *(--primes.upper_bound(b)) - *(primes.lower_bound(a))) << endl;
    }
    return 0;
}
