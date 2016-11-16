#include <bits/stdc++.h>

#define ll long long
using namespace std;

int main(){
	ll ans = 0;
	ll p;
	cin >> p;
	string n;
	cin >> n;
	for(int i = 0; i < n.length(); i++){
		if(n[i] == 'A'){
			ans++;
		} else {
			ans--;
		}
	}
	if (ans == 0){
		cout << "Friendship" << endl;
	} else if(ans < 0){
		cout << "Danik" << endl;
	} else {
		cout << "Anton" << endl;
	}
}