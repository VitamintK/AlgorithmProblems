#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int n, k, r;
	cin >> n >> k >> r;
	vector<int> cameras(n);
	for(int i = 0; i < k; i++){
		int house;
		cin >> house;
		cameras[house-1] = 1;
	}
	int p = 0;
	for(int i = 0; i < r; i++){
		p+= cameras[i];
	}
	int ans = 0;
	if(p == 0){
		cameras[r-1] = 1;
		ans++;
		p++;
	}
	if(p == 1){
		if(cameras[r-1]){
			cameras[r-2] = 1;
		} else {
			cameras[r-1] = 1;
		}
		ans++;
		p++;
	}
	for(int i = r; i < n; i++){
		if(cameras[i]){
			p++;
		}
		if(cameras[i-r]){
			p--;
		}
		if(p < 2){
			cameras[i] = 1;
			ans++;
			p++;
		}
	}
	cout << ans << endl;
	return 0;
}