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
    for(int t =0;t<T;t++){
        int n,l,r;
        cin >> n >> l >> r;
        vector<int> ls(n,0);
        vector<int> rs(n,0);
        int c;
        for(int i=0;i<l;i++){
            cin >> c;
            c--;
            ls[c]++;
        }
        for(int i=0;i<r;i++){
            cin >> c;
            c--;
            if(ls[c] >0){
                ls[c]--;
            } else {
                rs[c]++;
            }
        }
        int ans = 0;
        vector<int> evenl;
        vector<int> oddl;
        vector<int> evenr;
        vector<int> oddr;
        for(int i=0; i <n;i++){
            if(ls[i]>0){
                if(ls[i]%2){
                    oddl.push_back(ls[i]);
                    // cout << ls[i] << " pushed back" << endl;
                } else {
                    evenl.push_back(ls[i]);
                }
            } else if(rs[i]>0) {
                if(rs[i]%2){
                    oddr.push_back(rs[i]);
                } else {
                    evenr.push_back(rs[i]);
                }
            }
        }
        while(oddl.size()>0){
            int x;
            int y = oddl.back();
            if(oddr.size()>0){
                ans++;
                x = oddr.back();
                oddr.pop_back();
            } else if(evenr.size() > 0){
                ans++;
                x = evenr.back();
                evenr.pop_back();
            } else {
                break;
            }
            oddl.pop_back();
            if(x-1 >= 1){
                if((x-1)%2==0){
                    evenr.push_back(x-1);
                } else {
                    oddr.push_back(x-1);
                }
            }
            if(y-1 >= 1){
                if((y-1)%2==0){
                    evenl.push_back(y-1);
                } else {
                    oddl.push_back(y-1);
                }
            }
        }
        // cout << "processed lefts: " << ans << endl;
        while(oddr.size()>0){
            int x;
            int y = oddr.back();
            // cout << y << endl;
            if(oddl.size()>0){
                ans++;
                x = oddl.back();
                oddl.pop_back();
            } else if(evenl.size() > 0){
                ans++;
                x = evenl.back();
                evenl.pop_back();
            } else {
                break;
            }
            oddr.pop_back();
            if(x-1 >= 1){
                if((x-1)%2==0){
                    evenl.push_back(x-1);
                } else {
                    oddl.push_back(x-1);
                }
            }
            if(y-1 >= 1){
                if((y-1)%2==0){
                    evenr.push_back(y-1);
                } else {
                    oddr.push_back(y-1);
                }
            }
        }
        // cout << "processed rights: " << ans << endl;
        vector<int> lls;
        vector<int> rrs;
        for(int i =0; i < evenr.size();i++){
            rrs.push_back(evenr[i]);
        }
        for(int i =0; i < oddr.size();i++){
            rrs.push_back(oddr[i]);
        }
        for(int i =0; i < evenl.size();i++){
            lls.push_back(evenl[i]);
        }
        for(int i =0; i < oddl.size();i++){
            lls.push_back(oddl[i]);
        }
        int lres = 0;
        int rres = 0;
        // cout << lls.size() << "," << rrs.size() << endl;
        for(int i =0; i < lls.size();i++){
            ans += lls[i]/2;
            if(lls[i]%2){
                lres++;
            }
        }
        for(int i =0; i < rrs.size();i++){
            ans += rrs[i]/2;
            if(rrs[i]%2){
                rres++;
            }
        }
        // cout << lres << " " << rres << endl;
        ans += lres + rres;
        cout << ans << endl;
    }
	return 0;
}