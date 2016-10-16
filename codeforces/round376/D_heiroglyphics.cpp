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
//I READ THE PROBLEM WRONG REST IN PEACE ME
int main(){
	long long n, c;
	cin >> n >> c;
	long long l;
	long long preva;
	long long minn = -1;
	long long maxx = 9999999;
	long long a;
	for(long long i = 0 ; i < n; i++){
		cin >> l;
		bool still_increasing = true;
		long long x0;
		long long z0;
		long long z1;
		cin >> preva;
		x0 = preva;
		for(long long j = 1; j < l; j++){
			cin >> a;
			cout << a;
			if(still_increasing){
				if(a < preva){
					if(a >= x0){
						cout << -10 << endl;
						return 0;
					} else {
						still_increasing = false;
						z0 = a;
						z1 = a;
					}
				}
			} else {
				if(a < preva){
					cout << -11 << endl;
					return 0;
				} else {
					if(a >= x0){
						cout << -12 << endl;
						return 0;
					} else {
						z1 = a;
					}
				}
			}
		}
		//got our bounds for this word.  not intersect the ranges.
		if(!still_increasing){
			long long tempmin = c - x0;
			long long tempmax = c - x0 + x0 - z1;
			minn = max(minn, tempmin);
			maxx = min(maxx, tempmax);
			if(minn > maxx){
				cout << -13 << endl;
				return 0;
			}
		}
	}
	cout << minn << endl;
}