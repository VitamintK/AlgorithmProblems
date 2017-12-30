#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

double dist(double x1, double y1, double x2, double y2){
	return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
}

int main(){
	std::ios::sync_with_stdio(false);
	double n, r;
	cin >> n >> r;
	vector<int> xs(n);
	for(int i = 0; i < n; i++){
		cin >> xs[i];
	}
	vector<pair<double, double>> fxy;

	for(int i = 0 ; i < n; i++){
		double highest_y = r;
		for(int j = 0; j < fxy.size(); j++){
			//if(dist[fxy[j].first, ])
			double x2 = fxy[j].first;
			double csq = 4*r*r - (x2 - xs[i])*(x2-xs[i]);
			if(csq >= 0){
				highest_y = max(highest_y, sqrt(csq)+fxy[j].second);
			}
		}
		fxy.push_back(make_pair(xs[i], highest_y));
		cout << fixed;
  		cout << setprecision(10);
		cout << highest_y;
		if(i < n-1){ cout << " ";} else { cout << endl;}
	}
	return 0;
}