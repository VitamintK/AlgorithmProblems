//MODIFIED 8 QUEENS PROBLEM: https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2136
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
#include <utility>

using namespace std;

int n;
int q[15] = {0};
bool bad_r[15] = {0};
bool bad_ld[29] = {0};
bool bad_rd[29] = {0};
bool bad[15][15] = {0};
int amount = 0;

bool check(int col, int row){
	int rd = col + row;
	int ld = col - row + n - 1;
	if(bad_r[row] || bad_ld[ld] || bad_rd[rd] || bad[col][row]){
		return false;
	}
	q[col] = row;
	bad_ld[ld] = true;
	bad_rd[rd] = true;
	bad_r[row] = true;
}

void undo(int col, int row){
	int rd = col + row;
	int ld = col - row + n - 1;
	bad_ld[ld] = false;
	bad_rd[rd] = false;
	bad_r[row] = false;
}

void backtracking(int c){
	if(c == n){
		amount++;
		// for(int i = 0; i < n; i++){
		// 	cout << "queens: " << q[i] << " ";
		// }
		return;
	}
	for(int i = 0; i < n; i++){
		if(check(c, i)){
			backtracking(c+1);
			undo(c, i);
		}
	}
}

int main(){
	char p;
	cin >> n;
	int case_ = 0;
	while(n != 0){
		case_++;
		//for each test case
		amount = 0;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				cin >> p;
				if(p == '*'){
					bad[j][i] = true;
					//cout << "Bad: " << i << ", " << j << endl;
				}
			}
		}
		backtracking(0);
		cout << "Case " << case_ << ": " << amount << endl;
		cin >> n;
	}
}