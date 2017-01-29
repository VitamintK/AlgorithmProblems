#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	string s;
	cin >> s;
	vector<ll> rgyb(4);
	vector<ll> dead(4, 0);
	for(ll i = 0; i < s.length(); i++){
		if(s[i] == 'R')
			rgyb[0] = i%4;
		if(s[i] == 'G')
			rgyb[1] = i%4;
		if(s[i] == 'Y')
			rgyb[2] = i%4;
		if(s[i] == 'B')
			rgyb[3] = i%4;
		if(s[i] == '!')
			dead[i%4]++;
	}
	cout << dead[rgyb[0]] << " " << dead[rgyb[3]] << " " << dead[rgyb[2]] << " " << dead[rgyb[1]] << endl;
	return 0;
}