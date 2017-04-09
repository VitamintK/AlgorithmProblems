#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;
int main(){
	std::ios::sync_with_stdio(false);
	int a, b, c;
	cin >> a >> b >> c;
	int m;
	cin >> m;
	int x;
	string s;
	vector<pair<int, bool>> as; //the bool being true denotes USB.  false = PS/2.
	for(int i = 0; i < m; i++){
		cin >> x >> s;
		if(s == "USB"){
			as.push_back(make_pair(x, true));
		} else {
			as.push_back(make_pair(x, false));
		}
	}
	ll cost = 0;
	ll computers = 0;
	//sort all the mice in descending order of cost
	sort(as.rbegin(), as.rend());
	//iteratively pop the last element (cheapest mouse) from the vector, and decide to purchase it if
	//   we still have computers with the right port.
	while(!as.empty() && a+b+c > 0){
		pair<int, bool> p = as.back();
		as.pop_back();
		if(p.second == true){ //if the next cheapest is USB
			if(a > 0){
				cost+=p.first;
				a--;
				computers++;
			} else if(c > 0){
				cost+=p.first;
				c--;
				computers++;
			}
		} else { //or if the next cheapest is PS/2
			if(b > 0){
				cost+=p.first;
				b--;
				computers++;
			} else if(c > 0){
				cost+=p.first;
				c--;
				computers++;
			}
		}
	}
	cout << computers << " " << cost << endl;
	return 0;
}