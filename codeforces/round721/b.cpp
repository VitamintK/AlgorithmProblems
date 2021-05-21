// g++ -std=c++17 x.cpp && ./a.out
#include <iostream> 
#include <string> 
#include <set> 
#include <map> 
#include <stack> 
#include <queue> 
#include <vector> 
#include <utility> 
#include <iomanip> 
#include <sstream> 
#include <bitset> 
#include <cstdlib> 
#include <iterator> 
#include <algorithm> 
#include <cmath>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int T;
    cin >> T;
    for(int t=0;t<T;t++){
        int n;
        string s;
        cin >> n;
        cin >> s;
        int def = 0;
        int os = count(s.begin(),s.end(),'0');
        for(int i =0; i<n/2;i++){
            if(s[i] != s[n-1-i]){
                    def +=1;
            }
        }
        if(os == 2 && (n%2==1) && s[n/2]=='0'){
            cout << "DRAW" << endl;
            continue;
        }
        if(def == 0){
            // int endscore = 0;
            if(os == 0){
                cout << "DRAW" << endl;
            }
            else if(os != 1 && (n%2==1) && s[n/2]=='0'){
                // if(os%2==0){
                //     cout << "DRAW" << endl;
                // } else
                // if(os%4 == 1){
                //     cout << "BOB" << endl;
                // } else {
                cout << "ALICE" << endl;
                // }
            } else {
                cout << "BOB" << endl;
            }
            
            continue;
        }
        cout << "ALICE" << endl;
        continue;
    }
    
	return 0;
}