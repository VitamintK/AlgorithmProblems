#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		int t, m, n;
		cin >> t >> m >> n;
		vector<int> DP(n+1, 0);
		DP[0] = 1;
		int mm = 1;
		while(mm <= n){
			for(int j = 0; j < n+1; j++){
				if(j >= mm){
					DP[j] += DP[j-mm];
				}
			}
			mm*=m;
		}
		cout << t << " " << DP[n] << endl;
	}
	return 0;
}