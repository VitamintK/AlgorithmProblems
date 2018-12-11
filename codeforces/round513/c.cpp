#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <string>


#define ll long long
#define ull unsigned long long
using namespace std;

int main(){
	int n, m;
	cin >> n >> m;
	vector<int> as(n);
	vector<int> bs(m);
	vector<int> aspre(n);
	vector<int> bspre(m);
	vector<int> minsum_for_len(n+1, 212345678);

	for(int i = 0; i < n; i++){
		cin >> as[i];
		if(i == 0){
			aspre[i] = as[i];
		} else {
			aspre[i] = aspre[i-1] + as[i];
		}
		for(int j = 0; j <= i; j++){
			int len = i - j + 1;
			if(j == 0){
				minsum_for_len[len] = aspre[i];
			} else {
				minsum_for_len[len] = min(minsum_for_len[len], aspre[i] - aspre[j-1]);
			}
		}
	}

	for(int i = 0; i < m; i++){
		cin >> bs[i];
		if(i == 0){
			bspre[i] = bs[i];
		} else {
			bspre[i] = bspre[i-1] + bs[i];
		}
	}

	int x;
	cin >> x;

	map<int, int> distance_to_length;
	for(int i = 1; i < (int)(minsum_for_len.size()); i++){
		distance_to_length[minsum_for_len[i]] = i;
	}
	int ans = 0;
	for(int i = 0; i < m; i++){
		for(int j = 0; j <= i; j++){
			ll thasum;
			if(j == 0){
				thasum = bspre[i];
			} else {
				thasum = bspre[i] - bspre[j-1];
			}
			ll my_max = x/thasum;
			auto it = distance_to_length.upper_bound(my_max);

			if(it != distance_to_length.begin()){
				it--;
				// if(i == m-1 && j == 0){
				// 	cout << i-j+1 << " " << it->second << endl;
				// }
				ans = max(ans, (i-j+1)*((it)->second));
			}
		}
	}
	cout << ans << endl;
	return 0;
}