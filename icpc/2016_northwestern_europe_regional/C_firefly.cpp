#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;
ll xf, yf;

struct shield{
	bool operator()(shield a, shield b){
		return a.l < b.l;
	}
	ll l;
	ll u;
	double f;
};
vector<shield> shields;

double where(double dx){
	double y = 0;
	double x = 0;
	double delta_y;
	double delta_x;
	for(int i = 0; i < shields.size(); i++){
		//cout << shields[i].l << " " << shields[i].u << " " << shields[i].f << endl;
		
		if(shields[i].l > yf){
			//do this later
			delta_y = yf - y;
			delta_x = delta_y * dx;
			//cout << delta_y << " " << x << " " << delta_x << endl;
			return x + delta_x;
		}
		//to the shield!!!
		delta_y = shields[i].l - y;
		delta_x = delta_y * dx;
		x+= delta_x;
		y+=delta_y;
		//in the shield!!!
		double dxp = dx*shields[i].f;
		if(shields[i].u > yf){
			//do this later
			delta_y = yf - y;
			delta_x = delta_y * dxp;
			//			cout << "2: " << delta_y << " " << x << " " << delta_x << endl;

			return x+delta_x;
		} else {
			delta_y = shields[i].u - y;
			delta_x = delta_y * dxp;
			x+=delta_x;
			y+=delta_y;
		}
	}
	delta_y = yf - y;
	delta_x = delta_y * dx;
	return x + delta_x;
}

int main(){
	std::ios::sync_with_stdio(false);
	cin >> xf >> yf;
	ll n;
	cin >> n;
	for(ll i = 0; i < n; i++){
		ll l, u;
		double f;
		cin >> l >> u >> f;
		shield s;
		s.l = l; s.u = u; s.f = f;	
		shields.push_back(s);
	}
	sort(shields.begin(), shields.end(),shield());
	double lower = -100000;
	double upper = 100000;
	while(upper - lower > 0.00000000001){
		double mid = (lower+upper)/2;
		double abc = where(mid);
		//cout << "X is " << abc << endl;
		if(abc > xf){
			upper = mid;
		} else{
			lower = mid;
		}
	}
	cout.precision(10);

	cout << fixed << upper;
	return 0;
}	