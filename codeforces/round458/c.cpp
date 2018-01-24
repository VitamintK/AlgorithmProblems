#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	vector<int> path_len(1009);
	path_len[1] = 0;
	for(int i = 2; i < 1009; i++){
		int bcount = 0;
		int x = i;
		while(x!=0){
			if(x%2 == 1){
				bcount++;
			}
			x/=2;
		}
		//if(i < 100)
		//cout << i << ": " << path_len[bcount]+1 << endl	;
		path_len[i] = path_len[bcount]+1;
	}

	string s;
	cin >> s;
	int k;
	cin >> k;
	if(k == 0){
		cout << 1 << endl;
		return 0;
	}
	if(k == 1){
		cout << s.length() - 1 << endl;
		return 0;
	}
	ll MOD = 1000000007;
	// ll nck = 1;
	// for(int i = 1; i < s.length()-1; i++){
	// 	nck *= (n-i+1);
	// 	nck/=i;
	// 	//nck %= MOD;
	// 	if(path_len[i] == k-1){
			
	// 	}
	// }
	vector<vector<ll> > combos(1006, vector<ll>(1006, 0ll));
    for(int i = 0; i < 1006; i++){
        for(int j = 0; j < 1006; j++){
            if(j > i){
                combos[i][j] = 0ll;
            } else if (j == 0){
                combos[i][j] = 1ll;
            } else {
                combos[i][j] = (combos[i-1][j-1] + combos[i-1][j])%MOD;
            }
        }
    }
    // vector<ll> prefsum; //prefsum of n choose i
    // prefsum.push_back()
    // for(int i = 0; i < 1006; i++){

    // }
    ll ans = 0;
    // cout << "with first one" << endl;
    // for(int i = 1; i <= s.length() - 1; i++){
    // 	if(path_len[i] == k-1){
    // 		cout << i << " is " << k-1 << endl;
    // 		ans += combos[s.length()-1][i];
    // 		ans %= MOD;
    // 	}
    // }
    int mandatory_ones = 0;
    for(int i = 0; i < s.length(); i++){
    	if(s[i] == '1'){
    		//cout << "If we zero the " << i << "th bit..." << endl;
    		int l = s.length() - i - 1;
    		for(int j = 0; j <= l; j++){
    			if(path_len[j+mandatory_ones] == k-1 && j+mandatory_ones > 0){
    				//cout << "  then " << j << "+" << mandatory_ones << " makes " << k-1 << " for " << l << "C" << j << "=" << combos[l][j] << endl;
	    			ans += combos[l][j];
	    			ans %= MOD;
	    		}
    		}
    		mandatory_ones++;
    	}
    }
    if(path_len[mandatory_ones] == k-1){
    	ans++;
    	ans %= MOD;
    }
    cout << ans << endl;
	return 0;
}