#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main(){
	int seen_index = 0; //actually not seen yet
	string a;
	string b;
	cin >> a >> b;
	for (int i = 0; i < b.length(); i++){
		for(int j = seen_index+1; j<a.length(); j++){
			if(b[i] == a[j] && a[j] != a[seen_index]){
				cout << "FAIL" << endl;
				return 0;
			}
		}
		if(b[i] == a[seen_index]){
			if(seen_index == a.length()-1){
				cout <<"PASS" << endl;
				return 0;
			} else {
				seen_index++;
			}
		}
	}
	cout << "FAIL" << endl;
}