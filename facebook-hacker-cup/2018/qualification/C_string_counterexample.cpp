//Great problem

#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		string a;
		cin >> a;
		bool flag = false;
		int pos;
		for(int i = 1; i < a.length()-1; i++){
			if(a[i] == a[0]){
				flag = true;
				pos = i;
				break;
			}
		}
		bool diff_anywhere = false;
		string s = "";
		if(flag){
			for(int i = 0; i < 2; i++){
				for(int j = 0; j < pos; j++){
					s+=a[j];
				}
			}
			for(int i = pos; i < a.length(); i++){
				s+=a[i];
			}
			for(int i = 0; i < a.length(); i++){
				if(a[i] != s[i]){
					diff_anywhere = true;
				}
			}
		}
		if(flag && diff_anywhere){
			//cout << a << endl;
			cout << "Case #" << t+1 << ": " << s << endl;
		} else {
			cout  << "Case #" << t+1 << ": Impossible" << endl;
		}
	}
	return 0;
}