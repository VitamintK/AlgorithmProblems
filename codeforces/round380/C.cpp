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

	ll n, k, s, t;
	cin >> n >> k >> s >> t;
	vector<ll> sorted_fuels;
	vector<ll> fuels;
	vector<ll> prices;
	ll price, fuel;
	for(ll i = 0; i < n; i++){
		cin >> price >> fuel;
		fuels.push_back(fuel);
		sorted_fuels.push_back(fuel);
		prices.push_back(price);
	}
	vector<ll> stops(k);
	for(ll i = 0; i < k; i ++){
		cin >> stops[i];
	}
	sort(stops.begin(), stops.end());
	stops.push_back(s);
	k++;
	for(ll i = k-1; i >= 1 ; i--){
		stops[i] = stops[i] - stops[i-1];
	}
	sort(sorted_fuels.begin(), sorted_fuels.end());
	ll low = sorted_fuels[0];
	ll high = sorted_fuels[sorted_fuels.size() - 1];
	ll fasttime = 0;
		for(ll i = 0; i < k; i++){
			ll turbo = high - stops[i];
			if(turbo < 0){
				cout << -1 << endl;
				return 0;
			}
			fasttime += min(turbo, stops[i]) + (stops[i] - min(turbo, stops[i]))*2;
		}
		if(fasttime > t){cout << -1 << endl; return 0;}
	ll mid;
	bool fuck_binary_search = false;
	low = 0;
	sorted_fuels.push_back(10000000000000ll);
	high = sorted_fuels.size() -1;
	ll mid_;
	ll mid2;
	while(high - low >= 0){
		mid_ = (high + low + 1)/2;
		mid = sorted_fuels[mid_];
		if(mid_ == 0){
			break;
		}
		mid2 = sorted_fuels[mid_-1];
		//cout << mid << endl;
		ll fasttime = 0;
		for(ll i = 0; i < k; i++){
			ll turbo = mid - stops[i];
			if(turbo < 0){
				fasttime = t+1;
				break;
			}
			fasttime += min(turbo, stops[i]) + (stops[i] - min(turbo, stops[i]))*2;
		}
		ll fasttime2 = 0;
		for(ll i = 0; i < k; i++){
			ll turbo = mid2 - stops[i];
			if(turbo < 0){
				fasttime2 = t+1;
				break;
			}
			fasttime2 += min(turbo, stops[i]) + (stops[i] - min(turbo, stops[i]))*2;
		}
		if(fasttime <= t && fasttime2 > t){
			break;
		}
		if(fasttime > t){
			low = mid_ + 1;
		} else {
			high = mid_ -1;
		}
	}
	//cout << high << " " << low << endl;
	ll ans = 1e16;

	for(ll i = 0; i < fuels.size(); i++){
		if(fuels[i] >= sorted_fuels[mid_]){
			ans = min(ans, prices[i]);
		}
	}
	cout << ans << endl;
	return 0;
}