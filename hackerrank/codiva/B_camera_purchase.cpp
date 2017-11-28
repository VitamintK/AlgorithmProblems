//I think they wanted us to just put the cameras into 5 different lists and then just binary search for the cost of the kth cheapest
// camera with a given subset, but I thought it would be a fun challenge to preprocess everything, since only 5 camera companies
// means that the total number of subsets is 2^5 = 32.  Here, our preprocessing is an additional 32 O(n) processes
// , but querying is constant.  I couldn't get this accepted for the longest time because my magic constants weren't big enough >:(
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define ll long long

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    vector<vector<int> > cams(6);
    ll n;
    cin >> n;
    vector<ll> brands(n);
    for(ll i = 0; i < n; i++){
        cin >> brands[i];
    }
    for(ll i = 0; i < n; i++){
        ll a;
        cin >> a;
        cams[brands[i]].push_back(a);
    }
    for(ll i = 1; i <= 5; i++){
        sort(cams[i].begin(), cams[i].end());
    }
    vector<vector<ll> > rankings(32);
    for(ll i = 1; i < 32; i++){
        ll cnt = 0;
        vector<ll> pointers(6);
        ll flag = 0;
        for(ll j = 1; j <= 5; j++){
            if((i & (1<<(j-1)))==0){
                pointers[j] = 9234567899; 
            } else {
                if(cams[j].size() > 0){
                    pointers[j] = 0;
                    flag++;
                } else {
                    pointers[j] = 9234567899;
                }
            }
        }
        while(flag > 0){
            ll mindex;
            ll minvalue = 9234567899;
            for(int j = 1; j <= 5; j++){
                if(pointers[j] < cams[j].size() && cams[j][pointers[j]] < minvalue){
                    minvalue = cams[j][pointers[j]];
                    mindex = j;
                }
            }
            rankings[i].push_back(minvalue);
            pointers[mindex]++;
            if(pointers[mindex] >= cams[mindex].size()){
                flag--;
            }
        }
        //cout << i << " " << rankings[i].size() << endl;
        
    }
    int q;
    cin >> q;
    for(int i = 0; i < q; i++){
        ll d;
        cin >> d;
        ll bit = 0;
        for(ll j = 0 ; j < d; j++){
            ll a;
            cin >> a;
            bit |= (1 << (a-1));
        }
        //cout << bit << " bit" << endl;
        ll k;
        cin >> k;
        if(k > rankings[bit].size()){
            cout << -1 << endl;
        } else {
            cout << rankings[bit][k-1] << endl;
        }     
    }
    return 0;
}
