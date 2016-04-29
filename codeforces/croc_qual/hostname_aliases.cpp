#include <iostream>
#include <functional>
#include <string>
#include <unordered_map>
#include <utility>
#include <set>
#include <unordered_set>
using namespace std;
pair<string, string> split(string k){
	string f;
	string s;
	for(int i = 7; i < k.length(); i++){
		if(k[i] == '/'){
			f = k.substr(0, i);
			s = k.substr(i, 48);
			return make_pair(f, s);
		}
	}
	return (make_pair(k.substr(0, 48), ""));
}

int main(){

	long n;
	scanf("%ld", &n);
	unordered_map<string, long long> um;
	unordered_map<string, unordered_set<long long> > un;
	string k;
	//	cout << "d" << endl;

	for(long i = 0; i < n; i++){
	    char tmp[101];
        scanf("%100s", tmp);
        k= tmp;
		//scanf("%s", &k);
		pair<string, string> ss = split(k);
		//cout << ss.first << " " << ss.second << " " << hash<string>{}(ss.second) << endl;
		long long hsh = hash<string>{}(ss.second);
		long long temp = hsh;
		hsh << 16;
		hsh^= temp;
		hsh*=3644798167;
		if(un[ss.first].count(hsh) < 1){
		    um[ss.first] ^= hsh;
		    un[ss.first].insert(hsh);
		}
	}
	//		cout << "d" << endl;

	unordered_map<int, set<string> > b;
	for(const auto& i: um){
		b[i.second].insert(i.first);
	}
	//cout << "d" << endl;
	long fhu = 0;
	for(const auto& i: b){
		if(i.second.size() > 1){
			fhu++;
		}
	}
	cout << fhu << endl;
	for(const auto& i: b){
		if(i.second.size() > 1){
			for(const auto& j: i.second){
				cout << j << " ";
			}
			cout << endl;
		}
	}
	return 0;
}