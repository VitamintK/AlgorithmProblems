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
	int n;
	cin >> n;
	bool all_inc = true;
	bool all_dec = true;
	string prev;
	string name;
	cin >> prev;
	for(int i = 1; i < n; i++){
		cin >> name;
		if(prev < name){
			all_dec = false;
		}
		if(prev > name){
			all_inc = false;
		}
		prev = name;
	}
	if(all_inc && ! all_dec){
		cout << "INCREASING";
	} else if(all_dec && ! all_inc){
		cout << "DECREASING";
	} else {
		cout << "NEITHER";
	}
}