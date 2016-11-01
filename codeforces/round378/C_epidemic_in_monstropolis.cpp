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
	ll n;
	cin >> n;
	vector<ll> as(n);
	for(ll i = 0; i < n; i++){
		cin >> as[i];
	}
	ll m;
	cin >> m;
	vector<ll> bs(m);
	for(ll i = 0; i < m; i++){
		cin >> bs[i];
	}
	ll a_p = 0;
	ll l_p = 0;
	ll accum = 0;
	vector<pair<ll, char>> ans;
	for(ll i = 0; i < m; i++){
		ll max_val = 0;
		while(accum<bs[i]){
			if(a_p >= n){
				cout <<"NO" << endl;
				return 0;
			}
			max_val = max(max_val, as[a_p]);
			accum+=as[a_p];
			a_p++;
		}
		if(accum!= bs[i]){
			cout << "NO" << endl;
			return 0;
		}
		ll eater = -1;
		for(ll l = l_p; l < a_p; l++){
			if(as[l] == max_val){
				if(l > l_p && as[l-1] < max_val){
					eater = l-1;
					ans.push_back(make_pair(l-l_p+i, 'L'));
					break;
				} else if(l < a_p-1 && as[l+1] < max_val){
					eater = l;
					ans.push_back(make_pair(l-l_p+i, 'R'));
					break;
				}
			}
		}
		if(eater == -1 && a_p-l_p!=1){
			//out << l_p << " " << a_p << endl;
			cout << "NO" << endl;
			return 0;
		}
		if(a_p -l_p != 1){
		for(ll x = eater+1; x < a_p-1; x++){
			ans.push_back(make_pair(eater-l_p+i, 'R'));
		}
		for(ll x = eater; x >l_p; x--){
			ans.push_back(make_pair(x-l_p+i, 'L'));
		}
		}
		l_p = a_p;
		accum = 0;
	}
	if(a_p != n){
		cout << "NO" << endl;
		return 0;
	}
	cout <<"YES" << endl;
	for(ll i = 0; i < ans.size(); i++){
		cout << ans[i].first+1 << " " << ans[i].second << endl;
	}
}