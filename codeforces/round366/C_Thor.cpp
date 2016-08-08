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
	//http://web.mit.edu/sp.268/www/nim.pdf
	long long n;
	long long q;
	cin >> n >> q;
	int t;
	long long x;
	bool reads[300001];
	for(long i = 0; i < 300001; i++){
		reads[i] = false;
	}
	set<long long> apps[300001];
	long long cur_three = 0;
	long long ans = 0;
	long long notifs = 0;
	for(long long i = 0; i < q; i++){
		cin >> t >> x;
		if(t == 1){
			apps[x].insert(notifs);
			reads[notifs] = true;
			notifs++;
			ans++;
		} else if(t == 2){
			while(!apps[x].empty()){
				long long index = *apps[x].begin();
				//				cout << "*" << index << "*";
				if(index >= cur_three){
					reads[index] = false;
					ans--;
				}
				apps[x].erase(apps[x].begin());
			}
		} else {
			for(long long j = cur_three; j < x; j++){
				if(reads[j]){
					ans--;
				}
				reads[j] = false;
			}
			cur_three = max(cur_three, x);
		}
		cout << ans << endl;
	}
}