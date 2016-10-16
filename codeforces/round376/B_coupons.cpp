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
#include <set>
#include <queue>
#include <utility>

using namespace std;

int main(){
	long n;
	long a;
	cin >> n;
	bool active = false;
	for(long i = 0; i < n; i++){
		cin >> a;
		if(active){
			if(a == 0){
				cout << "NO" << endl;
				return 0;
			} else {
				a--;
			}
		}
		if(a%2 == 0){
			active = false;
		} else {
			active = true;
		}
	}
	if(active){
		cout << "NO" << endl;
		return 0;
	}
	cout << "YES" << endl;
	return 0;
}