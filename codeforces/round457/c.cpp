#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ll n, m;
	cin >> n >> m;

	int prime; 
	vector<int> sieve(110000);
	for(int i = 2; i < 110000; i++){
		if(sieve[i] == 0){
			if(i >= n-1){
				prime = i;
				break;
			}
			for(int j = i*2; j < 110000; j+= i){
				sieve[j] = 1;
			}
		}
	}

	// vector<vector<pair<int, ll> > > edges;
	// for(int i = 0; i < n-1; i++){
	// 	edges[i].push_back(make_pair(i+1, 1));
	// }
	// edges[n-1].push_back(make_pair(n, prime-(n-2)));

	cout << prime << " " << prime << endl;
	for(int i = 0; i < n-2; i++){
		cout << i+1 << " " << i+2 << " " <<  1<< endl;
	}
	cout << n-1 << " " << n << " " << prime - (n-2) << endl;
	int edgecount = n-1;
	for(int i = 0; i < n-1; i++){
		for(int j = i+2; j < n; j++){
			if(edgecount == m){
				return 0;
			}
			cout << i+1 << " " << j+1 << " " << 1000000000 << endl;
			edgecount++;
		}
	}
	return 0;
}