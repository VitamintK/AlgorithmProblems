#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;

vector<vector<int>> r0(vector<vector<int>> cube){
	vector<vector<int>> c = cube;
	for(int i = 0; i < 8; i++){
		c[2][(i+2)%8] = cube[2][i];
	}
	return c;
}

vector<vector<int>> r1(vector<vector<int>> cube){
	vector<vector<int>> c = cube;
	vector<int> x = {3,3,3,3,3,3,6,6};
	vector<int> y = {0,1,2,3,4,5,2,3};
	for(int i = 0; i < 8; i++){
		int j = (i+2)%8;
		c[y[i]][x[i]] = cube[y[j]][x[j]];
	}
	return c;
}

vector<vector<int>> r2(vector<vector<int>> cube){
	vector<vector<int>> c = cube;
	vector<int> x = {2,3,4,4,3,2,1,1};
	vector<int> y = {1,1,2,3,4,4,3,2};
	for(int i = 0; i < 8; i++){
		int j = (i+2)%8;
		c[y[i]][x[i]] = cube[y[j]][x[j]];
	}
	return c;
}

bool check(vector<vector<int>> c){
	vector<int> x = {2,3,2,3,2,3,2,3,2,3,2,3,0,1,0,1,4,5,4,5,6,7,6,7};
	vector<int> y = {0,0,1,1,2,2,3,3,4,4,5,5,2,2,3,3,2,2,3,3,2,2,3,3};
	for(int i = 0; i < 6; i++){
		for(int j = i*4; j < i*4 + 4; j++){
//			cout << i << " " << j << endl;
//			cout << c[0][2] << endl;
			if(c[y[i*4]][x[i*4]] != c[y[j]][x[j]]){
				return false;
			}
		}
	}
	return true;
}

int main(){
	std::ios::sync_with_stdio(false);
	vector<vector<int>> cube(8, vector<int>(8));
	vector<int> x = {2,3,2,3,2,3,2,3,2,3,2,3,0,1,0,1,4,5,4,5,6,7,6,7};
	vector<int> y = {0,0,1,1,2,2,3,3,4,4,5,5,2,2,3,3,2,2,3,3,2,2,3,3};
	for(int i = 0; i < 24; i++){
		cin >> cube[y[i]][x[i]];
	}
	int ans = 0;
	ans |= check(r0(cube));
	ans |= check(r0(r0(r0(cube))));
	ans |= check(r1(cube));
	ans |= check(r1(r1(r1(cube))));
	ans |= check(r2(cube));
	ans |= check(r2(r2(r2(cube))));
	if(ans){
		cout << "YES" << endl;
	} else {
		cout << "NO" << endl;
	}
	return 0;
}