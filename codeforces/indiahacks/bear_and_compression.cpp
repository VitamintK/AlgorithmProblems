#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
using namespace std;

int how_many(int len, char start, map<char, vector<string> >& cs){
	int ans = 0;
	if(len == 1){
		return 1;
	}
	for(auto i: cs[start]){
		ans+=how_many(len-1, i[0], cs);
	}
	return ans;
}

int main(){
	int n, q;
	cin >> n;
	cin >> q;
	map<char, vector<string> > cs;
	string s;
	char c;
	for(int i = 0; i < q; i++){
		cin >> s;
		cin >> c;
		cs[c].push_back(s);
	}
	char b = 'a';
	int g = how_many(n, b, cs);
	cout << g << endl;
	return 0;
}