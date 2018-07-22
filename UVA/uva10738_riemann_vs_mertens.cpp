#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	vector<int> sieve(1000003, -1); //sieve[x] contains x's largest prime factor
	//vector<int> is_square(1000003); //for convenience's sake.  we could also compute this on the fly.
	for(int i = 2; i < 1000003; i++){
		if(sieve[i] == -1){
			for(int j = i; j < 1000003; j+=i){
				sieve[j] = i;
			}
		}
	}

	vector<int> mu;
	mu.push_back(-2); //mu[0] is undefined
	mu.push_back(1);
	vector<int> M;
	M.push_back(0);
	M.push_back(1);
	for(int i = 2; i < 1000003; i++){
		int cnt = 0;
		int j = i;
		while(j != 1){
			if(j%(sieve[j]*sieve[j]) == 0){
				//we're dealing with a square number
				cnt = -1;
				break;
			}
			j/=sieve[j];
			cnt+=1;
		}
		if(cnt == -1){
			mu.push_back(0);
			M.push_back(M.back());
		} else {
			if(cnt%2==0){
				mu.push_back(1);
				M.push_back(M.back()+1);
			} else {
				mu.push_back(-1);
				M.push_back(M.back()-1);
			}
		}
	}

	int n;
	cin >> n;
	while(n != 0){

		cout.width(8); cout << right << setw(8) << n << right << setw(8) << mu[n] << right << setw(8) << M[n] << endl;
		cin >> n;
	}
	return 0;
}