//3D DP with 3d prefix sums.
//good exercise in thinking through inclusion-exclusion principle
//I think we did a problem almost exactly like this in IEEExtreme 2017(?)
#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

ll get_prefix_wo_corner(vector<vector<vector<ll>>> &dp3d, int i, int j, int k){
	ll psum = 0;
	psum += dp3d[i-1][j][k] + dp3d[i][j-1][k] + dp3d[i][j][k-1];
	psum -= dp3d[i-1][j-1][k];
	psum -= dp3d[i][j-1][k-1];
	psum -= dp3d[i-1][j][k-1];
	psum+=dp3d[i-1][j-1][k-1]; //hmmmmm
	return psum;
}

int main(){
	std::ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		int a, b, c;
		cin >> a >> b >> c;
		c++;a++;b++;
		vector<vector<vector<ll> > > pede(a, vector<vector<ll>>(b, vector<ll>(c, 0)));
		vector<vector<vector<ll> > > dp3d(a, vector<vector<ll>>(b, vector<ll>(c, 0)));
		for(int i = 1; i < a; i++){
			for(int j = 1; j < b; j++){
				for(int k = 1; k < c; k++){
					//cout << i << j<< k<< endl;
					ll x;
					cin >> x;
					pede[i][j][k] = x;
					//inclusion-exclusionnnnn shit how does this work again...
					//at this time I took 20 minutes to draw diagrams to figure it out
					//unfortunately, visualizing 3d on paper is hard as fuck
					//but I think I figured it out

					dp3d[i][j][k] = get_prefix_wo_corner(dp3d, i, j, k) + x;
				}
			}
		}

		ll ans = -12345678901234;
		for(int i = 1; i < a; i++){
			for(int j = 1; j < b; j++){
				for(int k = 1; k < c; k++){

					for(int I = 0; I < i; I++){
						for(int J = 0; J < j; J++){
							for(int K = 0; K < k; K++){

								ll negative = dp3d[I][j][k] + dp3d[i][J][k] + dp3d[i][j][K];
								negative -= dp3d[I][J][k] + dp3d[i][J][K] + dp3d[I][j][K];
								negative += dp3d[I][J][K];

								ll val = dp3d[i][j][k] - negative;
								if(val > ans){
								//	cout << i << j << k << endl << I << J << K << endl;
								}
								ans = max(ans, val);

							}
						}
					}

				}
			}
		}
		cout << ans << endl;
		if(t != T){
		 	cout << endl;
		}
	}
	return 0;
}