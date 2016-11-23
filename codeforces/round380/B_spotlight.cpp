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
	ll n, m;
	cin >> n >> m;
	vector<vector<int>> as(n,vector<int>(m));
	for(ll i = 0; i < n; i++){
		for(ll j = 0; j < m; j++){
			cin >> as[i][j];
		}
	}
	ll ans = 0;
	vector<vector<int>> ups(n,vector<int>(m));
vector<vector<int>> downs(n,vector<int>(m));
vector<vector<int>> lefts(n,vector<int>(m));
vector<vector<int>> rights(n,vector<int>(m));

	for(ll i = 0; i < n; i++){
		for(ll j = 0; j < m; j++){
			if(j > 0){
			lefts[i][j] = (as[i][j] | lefts[i][j-1]);
			}else {
				lefts[i][j] = as[i][j];
			}
			if(i > 0){
			ups[i][j] = (as[i][j] | ups[i-1][j]);
			}else {
				ups[i][j] = as[i][j];
			}
		}
	}
	for(ll i = n-1; i >=0; i--){
		for(ll j = m-1; j >= 0; j--){
			if(j <m-1){
			rights[i][j] = (as[i][j] | rights[i][j+1]);
			}else {
				rights[i][j] = as[i][j];
			}
			if(i < n-1){
			downs[i][j] = (as[i][j] | downs[i+1][j]);
			}else {
				downs[i][j] = as[i][j];
			}
		}
	}
	for(ll i = 0; i < n; i++){
		for(ll j = 0; j < m; j++){
			if(as[i][j] == 0){
				ans+=ups[i][j] + downs[i][j] + lefts[i][j] + rights[i][j];
			}
		}
	}
	cout << ans << endl;
	return 0;
}