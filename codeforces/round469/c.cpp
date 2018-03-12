#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	string s;
	cin >> s;
	vector<vector<int>* > trailing_zeroes;
	vector<vector<int>* > trailing_ones;
	for(int i = 0; i < s.length(); i++){
		int num = (s[i]=='1');
		//cout << i << endl;
		if(num == 0){
			if(trailing_ones.size() > 0){
				trailing_ones.back()->push_back(i);
				trailing_zeroes.push_back(trailing_ones.back());
				trailing_ones.pop_back();
			} else {
				//cout << "here" << endl;
				vector<int>* temp = new vector<int>;
				temp->push_back(i);
				//cout <<"worker" << endl;
				trailing_zeroes.push_back(temp);
			}
		} else {
			if(trailing_zeroes.size() > 0){
				trailing_zeroes.back()->push_back(i);
				trailing_ones.push_back(trailing_zeroes.back());
				trailing_zeroes.pop_back();
			} else {
				cout << "-1" << endl;
				return 0;
			}
		}
	}
	if(trailing_ones.size() > 0){
		cout << "-1" << endl;
		return 0;
	}
	cout << trailing_zeroes.size() << endl;
	for(int i = 0; i < trailing_zeroes.size(); i++){
		cout << trailing_zeroes[i]->size();
		for(int j = 0; j < trailing_zeroes[i]->size(); j++){
			cout << " " << (*trailing_zeroes[i])[j]+1;
		}
		cout << endl;
	}
	return 0;
}