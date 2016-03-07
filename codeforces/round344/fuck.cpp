#include <iostream>
#include <vector>
#include <string>
#include <utility>
using namespace std;
int main(){
	int n, m;
	cin >> n;
	cin>>m;
	vector< pair<int, char> > s;
	vector< pair<int, char> > t;
	int a;
	char b;
	for(int i = 0; i < n; i++){
		cin >>a;
		cin >>b;
		cin>>b;
		t.push_back(pair<int,char>(a,b));
	}
	for(int i = 0; i < m; i++){
		cin >>a;
		cin >>b;
		cin>>b;
		s.push_back(pair<int,char>(a,b));
	}
	char l = '.';
			cout <<"here";

	for(int i = 0; i < s.size(); i++){
		if(l == s[i].second){
			l = s[i].second;
			s[i-1].first+=s[i].first;
			s.erase(s.begin() + i); 
			i = i - 1;
		} else {
			l = s[i].second;
		}
		cout <<"here";
	}
	for(int i = 0; i < t.size(); i++){
		if(l == t[i].second){
			l = t[i].second;
			t[i-1].first+=t[i].first;
			t.erase(t.begin() + i);

			i = i - 1;
		} else {
			l = t[i].second;
		}
	}
	//cout << "size: " << t.size() << endl;
		int goods = 0;

	if(s.size() == 1){
		cout <<"here";
		for(int i = 0; i < t.size(); i++){
			if(t[i].second == s[0].second && t[i].first >= s[0].first){
				goods+= t[i].first + 1 - s[0].first;
			}
		}
		cout <<"here";
	} else {
		for(int i = 0; i < t.size(); i++){
			for(int j = 0; j<s.size(); j++){
				if(j == 0 || j == s.size() -1){
					if(s[j].second != t[i+j].second){
						//cout << "Break" << endl;
						break;}
						//cout << s[j].second << ": " << t[i+j].second << endl;
					if(j == s.size() -1){
						//cout << j << " " << i << endl;
						goods++;
					}
				} else {
					if(s[j].second != t[i+j].second || s[j].first != t[i+j].first){
						//cout <<"! " << j << " " << i << endl;

						break;
					}
				}
			}
		}
	}
	cout << goods;

	return 0;
}