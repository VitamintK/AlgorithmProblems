#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
using namespace std;

double dist(double x1, double y1, double x2, double y2){
	return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
}

struct node{
	double x, y;
} a[5000];

int main(){
	std::ios::sync_with_stdio(false);
	double n, r;
	cin >> n >> r;

	vector<int> vis(2000);
	//copy pasting someone else's to hack
	double x;
	for(int i = 1; i <= n; i++){
		cin >> x;
		double tmp = 0;
		int id = 0;
		for(int j = x-r; j<= x+r; j++) if(j>=0){
			int k = vis[j];
			if(tmp < a[k].y){
				id = k;
				tmp = a[k].y;
			}
		}
		
		a[i].x = x;
		if(id == 0){
			a[i].y = r;
		} else {
			a[i].y = a[id].y + sqrt(4*r*r - abs(x-a[id].x)*abs(x-a[id].x));
		}
		for(int j = x-r; j <= x+r; j++){
			vis[j] = i;
		}
		cout << a[i].y << " ";
	}
	return 0;
}