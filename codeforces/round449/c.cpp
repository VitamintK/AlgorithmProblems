#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

vector<ll> lengths;

char get_ans(ll n, ll k){
	if(n == 0){
		if(k > lengths[n]){
			return '.';
		} else {
			return "What are you doing at the end of the world? Are you busy? Will you save us?"[k-1];
		}
	}
	if(n < lengths.size() && k > lengths[n]){
		return '.';
	}
	if(k <= 34){
		return "What are you doing while sending \""[k-1];
	} else if(n > lengths.size() || k <= 34 + lengths[n-1]){
		return get_ans(n-1, k-34);
	} else if(k <= 34 + lengths[n-1] + 32){
		return "\"? Are you busy? Will you send \""[k-34-lengths[n-1]-1];
	} else if(k <= 34 + lengths[n-1] + 32 + lengths[n-1]){
		return get_ans(n-1, k - 34 - lengths[n-1] - 32);
	} else {
		return "\"?"[k - 34 - lengths[n-1] - 32 - lengths[n-1] - 1];
	}
}

int main(){
	std::ios::sync_with_stdio(false);
	lengths.push_back(75);
	for(ll i = 0; i < 53; i++){
		lengths.push_back(lengths.back()*2 + 68);
		//cout << lengths.back() << endl;
	}
	int q;
	cin >> q;
	ll n, k;
	//vector<char> ans;
	for(int i = 0; i < q; i++){
		cin >> n >> k;
		cout << get_ans(n, k);
	}
	cout << endl;
	return 0;
}