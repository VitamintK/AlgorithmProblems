#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

vector<pair<int, pair<int, int>  > > v;

vector<int> ans;
ll T;

bool f(int probs){
	long long tt = 0;
	ans.clear();
	int num = 0;
	for(int i = 0; i < v.size() && num < probs; i++){
		if(v[i].second.first >= probs && v[i].first + tt <= T){
			ans.push_back(v[i].second.second);
			tt += v[i].first;
			num++;
		}
	}
	//cout << probs << " " << num << endl;
	return (num >= probs);
}
int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin >> n >> T;
	for(int i = 0; i < n; i++){
		int a, t;
		cin >> a >> t;
		v.push_back(make_pair(t,make_pair(a, i)));
	}
	sort(v.begin(), v.end());
	int hi = n;
	int lo = 0;
	int mid = n/2;
	while(hi > lo){
		mid = lo + (hi - lo + 1)/2;
		if(f(mid)){
			//cout << mid << "  worked" << endl;
			lo = mid;
		} else {
			hi = mid - 1;
		}
	}

	f(lo);
	cout << lo << endl << ans.size() << endl;
	for(int i = 0 ; i < ans.size(); i++){
		cout << ans[i]+1 << " ";
	} cout << endl;

	return 0;
}