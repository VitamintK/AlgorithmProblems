#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	string s1;
	string s2;
	int fl = 0;
	while(cin >> s1){
		if(fl != 0){ cout << endl;}
		fl = 1;
		cin >> s2;
		vector<int> s3(105);
		for(int i = 0; i < max(s2.length(), s1.length()); i++){
			if(i < s2.length() && s2[s2.length()-1-i]=='1'){
				s3[s3.size()-1-i]++;
			}
			if(i < s1.length() && s1[s1.length()-1-i]=='1'){
				s3[s3.size()-1-i]++;
			}
		}


		while(true){
			bool flag = false;
			for(int i = 0; i < s3.size(); i++){
				if(i > 0 && s3[s3.size()-1-i] > 0 && s3[s3.size()-1-i+1] > 0){
					//adjacent numbers
					//00110 ->
					//01000
					s3[s3.size()-1-i]--;
					s3[s3.size()-1-i+1]--;
					s3[s3.size()-1-i-1]++;
					flag = true;
				}
				while(s3[s3.size()-1-i] > 1){
					s3[s3.size()-1-i]-=2;
					s3[s3.size()-1-i-1]+=1;
					if(i > 1){
						s3[s3.size()-1-i+2]+=1;
					}
					else if(i == 1){
						s3[s3.size()-1]++;
					}
					else if(i == 0){

					}
					flag = true;
				}
			}
			if(!flag){
				break;
			}
		}
		bool flag = false;
		for(int i = 0; i < s3.size(); i++){
			if(s3[i] == 1){
				cout << 1;
				flag = true;
			} else {
				if(flag){
					cout << 0;
				}
			}
		}

		if(flag == false){
			cout << 0;
		}
		cout << endl;
	}
	return 0;
}