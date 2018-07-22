//Great problem

#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	string s1;
	string s2;

	vector<ull> fibs;
	ull f1 = 1;
	ull f2 = 1;
	for(int i = 0; i < 110; i++){
		fibs.push_back(f2);
		cout << f2 << endl;
		f1 = f1+f2;
		swap(f1, f2);
	}

	while(cin >> s1){
		cin >> s2;
		int n1 = 0;
		int n2 = 0;
		for(int i = 0; i < s1.length(); i++){
			if(s1[s1.length()-1-i] == '1'){
				n1+=fibs[i];
			}
		}
		for(int i = 0; i < s2.length(); i++){
			if(s2[s2.length()-1-i] == '1'){
				n2+=fibs[i];
				cout << n2 << endl;
			}
		}
		int n3 = n1+n2;
		cout << n3 << endl;
		string s3 = "";
		bool flag = false;
		for(int i =fibs.size()-1; i>=0; i--){
			if(fibs[i] <= n3){
				flag = true;
				s3+="1";
				n3-=fibs[i];
			} else {
				if(flag){
					s3+="0";
				}
			}
		}
		cout << s3 << endl;
	}
	return 0;
}