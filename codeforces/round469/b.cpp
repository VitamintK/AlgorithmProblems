#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int n, m;
	cin >> n >> m;
	vector<int> xs(123456);
	vector<int> ys(123456);
	for(int i = 0; i < n; i++){
		cin >> xs[i];
	}
	for(int i = 0; i < m; i++){
		cin >> ys[i];
	}

	//ll point_x = 0;
	int point_y = 0;
	ll value_x = 0;
	ll value_y = 0;
	int ans = 0;
	for(int i = 0; i < n; i++){
		value_x += xs[i];
		while(value_y < value_x){
			value_y += ys[point_y];
			point_y++;
		}
		if(value_y == value_x){
			ans++;
		}
	}
	cout << ans << endl;
	return 0;
}