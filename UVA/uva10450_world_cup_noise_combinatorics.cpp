//interesting problem!
//there's probably a closed-form solution?  one that involves combinations/permutations perhaps
//but the dp solution is very simple.  Plus, they probably have the same complexity.
//I would love to know a mathematical expression for this problem though.
#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	vector<ll> DPz;
	vector<ll> DPo;

	//compute the DP table
	DPz.push_back(1);
	DPo.push_back(1);
	for(int i = 1; i < 51; i++){
		ll z = DPz[i-1] + DPo[i-1];
		ll o = DPz[i-1];
		DPz.push_back(z);
		DPo.push_back(o);
	}

	//print the solutions
	int T;
	cin >> T;
	for(int t = 0; t < T; t++){
		int n;
		cin >> n;
		cout << "Scenario #" << t+1 << ":" << endl;
		cout << DPz[n-1] + DPo[n-1] << endl << endl;
	}
	return 0;
}