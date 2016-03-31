#include <iostream>
#include <unordered_map>
using namespace std;
int main(){
	long n;
	int k;
	unordered_map<int, int> ans
	int best = 0;
	int best_id = 0;
	cin >> n;
	for(long i = 0; i < n; i ++){
		cin >> k;
		ans[k]++;
		if(ans[k] > best){
			best = ans[k];
			best_id = k;
		}
	}
	cout << best_id << endl;
	return 0;
}