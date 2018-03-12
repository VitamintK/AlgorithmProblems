#include <bits/stdc++.h>

using namespace std;


int main() {
    int n;
    cin >> n;
    string s;
    map<int, long long> counts;
    for(int i = 0; i < n; i++){
        cin >> s;
        int mask = 0;
        for(int j = 0; j < s.length(); j++){
            mask |= (1 << (s[j]-'0'));
        }
        //cout << s << ": " << mask << endl;
        counts[mask]++;
    }
    long long ans = 0;
    for(int i = 0; i < 1024; i++){
        for(int j = i; j < 1024; j++){
            if((i|j) == 1023){
                if(i == j){
                    ans += (counts[i]*(counts[i]-1))/2;
                } else {
                    ans += counts[i]*counts[j];
                    //if(counts[i]*counts[j] > 0){
                    //    cout << i << " " << j << endl;
                    //}
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}
