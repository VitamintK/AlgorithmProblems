#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	int n, k;
	cin >> n >> k;
	string s;
	cin >> s;
	map<char, int> last_occurences;
	string all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	for(int i = 0; i < 26; i++){
		last_occurences[all_letters[i]] = -1; 
	}
	for(int i = n-1; i >= 0; i--){
		if(last_occurences[s[i]] == -1){
			last_occurences[s[i]] = i;
		}
	}
	set<char> open;
	for(int i = 0; i < n; i++){
		open.insert(s[i]);
		if(open.size() > k){
			cout << "YES" << endl;
			return 0;
		}
		if(last_occurences[s[i]] == i){
			open.erase(s[i]);
		}
	}
	cout << "NO" << endl;
	return 0;
}