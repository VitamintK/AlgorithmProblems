#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	string s;
	cin >> s;
	vector<int> pre(s.length());
	vector<int> suf(s.length());
	pre[0] = (s[0] == '(');
	for(int i = 1; i < s.length(); i++){
		if(s[i] == '('){
			pre[i] = pre[i-1]+1;
		} else {
			pre[i] = pre[i-1];
		}
	}
	suf[s.length()-1] = (s[s.length()-1] == ')');
	for(int i = s.length()-2; i >= 0; i--){
		if(s[i] == ')'){
			suf[i] = suf[i+1]+1;
		} else {
			suf[i] = suf[i+1];
		}
	}
	ll ans = 0;
	for(int i = 0; i < s.length(); i++){
		cout << pre[i] << ' ';
		ans+= min(suf[i], pre[i]);
		ans%=1000000007;
	} cout << endl;
	for(int i = 0; i < s.length(); i++){
		cout << suf[i] << ' ';
	} cout << endl;
	cout << ans << endl;
	return 0;
}