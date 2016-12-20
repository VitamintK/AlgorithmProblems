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
	char a;
	cin >> n >> m;
	vector<vector<ll>> grid (n, vector<ll>(m));
	ll minrow = 100000000;
	ll mincol = 100000000;
	ll maxrow = -1;
	ll maxcol = -1;
	for(ll i = 0; i < n; i++){
		for(ll j = 0; j < m; j++){
			cin >> a;
			if(a == 'X'){
				grid[i][j] = 1;
				minrow = min(i, minrow);
				maxrow = max(i, maxrow);
				mincol = min(j, mincol);
				maxcol = max(j, maxcol);
			} else {
				grid[i][j] = 0;
			}
		}
	}
	//cout << minrow << " " << mincol << " " << maxrow << " " << maxcol << endl;
	for(ll i = minrow; i <= maxrow; i++){
		for(ll j = mincol; j <= maxcol; j++){
			if(grid[i][j] == 0){
				cout << "NO" << endl;
				return 0;
			}
		}
	}
	cout << "YES" << endl;
	return 0;
}