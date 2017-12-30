#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n;
	vector<ll> piles(n);
	
	vector<ll> squares;
	ll x = 0;
	while(true){
		if(x*x < 100000000000){
			squares.push_back(x*x);
		} else {
			break;
		}
		x++;
	}
	//cout << squares.size() << endl;

	ll num_of_squares = 0;
	vector<ll> smallest_diffs;
	vector<ll> smallest_to_be_not_a_square;
	for(ll i = 0; i < n; i++){
		cin >> piles[i];
		if(piles[i] == 0){
			smallest_to_be_not_a_square.push_back(2);
			num_of_squares+=1;
			continue;
		}
		auto candidate = lower_bound(squares.begin(), squares.end(), piles[i]);
		if(*candidate == piles[i]){
			//we are a square!
			smallest_to_be_not_a_square.push_back(1);
			num_of_squares+=1;
		}else {
			//not a square!
			auto other_candidate = --lower_bound(squares.begin(), squares.end(), piles[i]);
			smallest_diffs.push_back(min(abs(*other_candidate - piles[i]), abs(*candidate - piles[i])));
		}
	}


	if(num_of_squares == n/2){
		cout << 0 << endl;
	} else if(num_of_squares > n/2){
		ll ans = 0;
		sort(smallest_to_be_not_a_square.begin(), smallest_to_be_not_a_square.end());
		for(ll i = 0; i < num_of_squares - n/2; i++){
			ans += smallest_to_be_not_a_square[i];
		}
		cout << ans << endl;
	} else {
		ll ans = 0;
		sort(smallest_diffs.begin(), smallest_diffs.end());
		for(ll i = 0; i < n/2 - num_of_squares; i++){
			ans += smallest_diffs[i];
		}
		cout << ans << endl;
	}

	return 0;
}