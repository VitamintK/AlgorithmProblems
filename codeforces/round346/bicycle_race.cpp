#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;


int main(){
	long n;
	cin >> n;
	long x, y;
	int first = 0;
	int direction;
	int last;
	long lx, ly;
	long ans = 0;
	for(long i = 0; i < n; i++){
		cin >> x >> y;
		if(x > lx){
			direction = 1;
		} else if(y > ly){
			direction = 2;
		} else if(x < lx){
			direction = 3;
		} else {
			direction = 4;
		}
		if(first>1){
			if(direction == (last)%4 + 1){
			    //cout << x << " " << y << endl;
				ans++;
			}
		}
		lx = x;
		ly = y;
		last = direction;
		first++;
	}
	cout << ans;
	return 0;
}