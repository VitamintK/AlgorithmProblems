#include<bits/stdc++.h>

using namespace std;


int main(){
    int C = 10;
    vector<int> us(10);
    vector<int> rs(10);
    vector<int> ts(10);

    vector<int> my_us(10);
    vector<int> my_rs(10);
    for(int i = 0; i < C; i++){
        cin >> my_us[i] >> my_rs[i];
    }
    for(int i = 0; i < C; i++){
        cin >> us[i] >> rs[i] >> ts[i];
    }

    int c = 0;
    int m = 0;
    int t = 0;
    while(c < 3){
        int cycle = us[m]+rs[m];
        if(t < ts[m]){
            t = t + my_us[m] + my_rs[m];
            if(t - my_rs[m] > ts[m]){
                ts[m] = t - my_rs[m];
            }
        } else {
            int wait;
        //    cout << "ts[m] is " << ts[m] << endl;
            if((t - ts[m])%cycle < us[m]){
                wait = t+us[m] - (t-ts[m])%cycle;
        //        cout << "need to wait! until " << wait << endl;
            } else {
                wait = t;
            }
            ts[m] = max(wait+my_us[m], t - (t-ts[m])%cycle + cycle);
            t = wait + my_us[m] + my_rs[m];
        }
       // cout << "after doing and recovering from C " << c << " M " << m << " we at time " << t << endl;


        m++;
        if(m == C){
            m = 0;
            c++;
        }
    }
    cout << t - my_rs[C-1] << endl;
    return 0;
}