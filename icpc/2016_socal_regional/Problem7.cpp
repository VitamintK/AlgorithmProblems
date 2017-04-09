#include <bits/stdc++.h>

#define REP(i,a,b) for(int i = (a); i < b; i++)
typedef long long ll;
using namespace std;


template <class T>
int to_int(T &s){
	int to_return;
	stringstream SS;
	SS << s;
	SS >> to_return;
	return to_return;
}


int main(){
	string s;
	int data[100001];
	int N = 0;
	memset(data, 0, sizeof(data));
	while(cin >> s){
		if ('0' <= s[0] && s[0] <= '9')
			data[N++] = to_int(s);
		else
			break;
	}
	
	if (cin.eof()) return 0;
	
	int a,b,c;
	while(true){
		if (s == "A"){
			cin >> a;
			swap(data[a], data[a+1]);
		}
		else if (s == "Q"){
			cin >> a >> b >> c;
			vector<int> n;
			for(int i = a; i <= b; i++) n.push_back(data[i]);
			sort(n.begin(), n.end());
			cout << n[c] << '\n';
		}
		
		if (!(cin >> s))
			break;
	}

	
}
