#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

long long h;

long long dpt[10001][101] = {0};

// long long dp(long long n, long long w){
// 	//cout << n << " " << w << endl;
// 	if(w == 0){
// 		if(n == 0){
// 			return 1;
// 		} else {
// 			return 0;
// 		}
// 	}
// 	if(dpt[n][w] > 0){
// 		return dpt[n][w];
// 	}
// 	long long ans = 0;
// 	for(long long i = 0; i <= min(h, n); i++){
// 		ans+= dp(n-i, w-1);
// 		ans = ans%1000000007;
// 	}
// 	dpt[n][w] = ans;
// 	return ans;
// }

int main(){


	long long n, w;
	cin >> n >> w >> h;
	for(int i = 0; i <= 100; i++){
		dpt[0][i] = 1;
	}
	for(int i = 0; i <= 10000; i++){
		dpt[i][0] = 0;
	}
	dpt[0][0] = 1;

	long long rans =0;
	long long ans;
	for(long long i = 1; i <= n; i++){
		for(long j = 1; j <= w; j++){
			if(i ==0 && j==0){
				continue;
			}
			ans = 0;
			for(long k = 0; k <= min(i,h); k++){
				ans += dpt[i-k][j-1];
				ans = ans%1000000007;
			}
			dpt[i][j] = ans;
			if(j == w){
				rans+= ans;
				rans = rans%1000000007;
			}
		}
	}


	for(int i = 0; i < 5; i++){
		for(int j = 0; j < 5; j++){
			//cout << i << "," << j << ": " << dpt[i][j] << endl;
		}
	}
	// long long ans = 0;
	// for(long i = 0; i <= n; i++){
	// 	ans += dp(i, w);
	// 	ans = ans % 1000000007;
	// }

	rans = rans - min((n/w), h);
	rans += 1000000007;


	cout << rans % 1000000007;


	return 0;
}