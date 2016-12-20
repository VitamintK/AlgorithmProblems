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
#define ll long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll n, k;
	cin >> n >> k;
	ll snow_days = 0;
	ll changes = 0;
	bool snow = false;
	ll a;
	vector<double> no_snows;
	ll current_no_snow = 0;
	for(ll i = 0; i < n; i++){
		cin >> a;
		if(a < 0){
			snow_days++;
			if(snow == false){
				if(no_snows.size() > 0){
				no_snows.push_back(current_no_snow);
				} else {
					no_snows.push_back(0);
				}
				current_no_snow = 0;
				snow = true;
				changes++;
			}
		} else {
			current_no_snow++;
			if(snow == true){
				snow = false;
				changes++;
			}
		}
	}
	if(snow_days > k){
		cout << -1 << endl;
		return 0;
	}
	//cout << changes << endl;
	//no_snows.push_back(current_no_snow+0.1);
	sort(no_snows.begin(), no_snows.end());
	//bool end;
	for(ll i =0; i < no_snows.size(); i++){
		//cout << no_snows[i] << "x" << endl;
		//if(no_snows[i] > (ll)(no_snows[i])){
		//	no_snows[i] = (ll)(no_snows[i]);
		//	end = true;
		//	cout << "end! " << no_snows[i] << endl;
		//} else {
		//	end = false;
		//}
		if(snow_days + no_snows[i] <= k && no_snows[i] > 0){
			//if(end){
			//	cout << "end" << endl;
			//	changes-=1;
			//} else {
			//	cout <<"not end " << no_snows[i] << endl;
				changes-=2;
			//}
			snow_days += no_snows[i];
		}
	}
	if(current_no_snow > 0){
		if(snow_days + current_no_snow <= k && current_no_snow != n){
			changes--;
		}
	}
	cout << changes << endl;
}