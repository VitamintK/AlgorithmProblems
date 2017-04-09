#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

int main(){
	int t;
	string p;
	cin >> t;
	for(int i = 0; i < t; i++){
		int ans = 0;
		char prev = 'o';
		char now = 'o';
		cin >> p;
		for(int j = 0; j < p.size(); j++){
			now = p[j];
			if((now == '-' && prev == '+' )|| (now == '+' && prev == '-' )){
				ans++;
			}
			prev = now;
		}
		if (now == '-'){
			ans++;
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}


	return 0;
}