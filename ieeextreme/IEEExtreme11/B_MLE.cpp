#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#define ll long long

using namespace std;
int main() {
    int t;
    ll a, b;
    cin >> t >> a >> b;
    int maxn = 1000001;
    vector<int> lower_sieve(maxn+1);
    for(ll i = 0; i < maxn; i++){
        lower_sieve[i] = i;
    }
    //vector<ll> sieve(b+1-a);
    //for(ll i = 0; i < b+1-a; i++){
    //    sieve[i] = i+a;
    //}
    vector<map<ll, int> > factormaps(b+1-a);
    for(ll i = 2; i < maxn; i++){
        if(lower_sieve[i] == i){
            for(ll j = i*2; j < maxn; j+=i){
                //if(lower_sieve[j] == j){
                    lower_sieve[j] = i;
                //}
            }
            for(ll j = i * ((a+i-1)/i); j <= b; j+=i){
//                cout << j-a << endl;
                //if(sieve[j-a] == j){
                factormaps[j-a][i]++;
                //    sieve[j-a] = i;
                //}
            }
        }
    }
    //for(ll i = 0; i < 10; i++){
    //    cout << i << " " << lower_sieve[i] << endl;
    //}
        //cout << factormaps[3].size() << endl;

    //std::map<int, int> test;
    //test[1] = 0;
    //cout << test[1] << endl;
    for(int i = 0; i < t; i++){
        //cout << "starting" << endl;
        ll d;
        ll ans = 0;
        cin >> d;
        for(ll n = a; n <= b; n++){
            //cout << "n: " << n << endl;
            ll nn = n;
            //cout << 50 << endl;
            ll sub_ans = 1;
            //cout << n << " " << factormaps[n].size() << endl;
            for(auto it = factormaps[n-a].begin(); it != factormaps[n-a].end(); it++){
                //cout << it->first << ": " << it->second << endl;
                if(it->first != d){
                    sub_ans *= (it->second + 1);
                }
                nn/= pow(it->first, it->second);
            }
            //cout << n << endl;
            //sub_ans--;
            if(nn != 1){
                sub_ans++;
            }
            ans+=sub_ans;
            //cout << ans << endl;
        }
        cout << ans << endl;
    }
    return 0;
}