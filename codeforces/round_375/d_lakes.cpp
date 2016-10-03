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


int main(){
	int n, m, k;
	cin >> n >> m >> k;
	pair<int,int> lakes[1000];
	//vector<int> lake_substance;
	int actual_lakenum = 0;
	int lakenum = 0;
	int mp[50][50];
	char l;
	for(int i = 0; i < n; i++){
		for(int j =0; j < m; j++){
			cin >> l;
			if(l == '.'){
				mp[i][j] = -1;
			} else {
				mp[i][j] = -2;
			}
		}
	}
	vector<pair<int, int>> to_ex;
	int size = 0;
	for(int i = 0; i < n; i++){
		for(int j =0; j < m; j++){
			if(mp[i][j] == -1){
				//cout << lakenum << " " << actual_lakenum << endl;
				bool is_not_actually_a_lake = false;
				size = 0;
				mp[i][j] = lakenum;
				size++;
				to_ex.push_back(make_pair(i+1, j));
				to_ex.push_back(make_pair(i, j+1));
				if(i == 0 || i == n-1 || j == 0 || j == m -1){
					is_not_actually_a_lake = true;
				} 
					while(!to_ex.empty()){
						pair<int,int> ex = to_ex.back();
						to_ex.pop_back();
						int y = ex.first;
						int x = ex.second;
						
						if(mp[y][x] == -1){
							if(y == 0 || y == n-1 || x == 0 || x == m -1){
								is_not_actually_a_lake = true;
							}
							mp[y][x] = lakenum;
							size++;
							to_ex.push_back(make_pair(y+1, x));
							to_ex.push_back(make_pair(y, x+1));
							to_ex.push_back(make_pair(y-1, x));
							to_ex.push_back(make_pair(y, x-1));
						}
					
				}
				if(is_not_actually_a_lake){
					//cout << lakenum << " not actually a lake" << endl;
					lakenum++;
				} else {
					lakes[actual_lakenum] = make_pair(size,lakenum);
					lakenum++;
					actual_lakenum++;
				}
			}
		}
	}
	// for(int i = 0; i < 50; i++){
	// 	cout << lakes[i].second << ":" << lakes[i].first << ", ";
	// } cout << endl;
	// for(int i = 0; i < n; i++){
	// 	for(int j = 0; j < m; j++){
	// 		if(mp[i][j] == -2){
	// 			cout << "*";
	// 		} else {
	// 			cout << mp[i][j] ;
	// 		}
	// 	} cout << endl;
	// }
	sort(lakes, lakes+(actual_lakenum));
	int summation = 0;
	for(int i =0; i < (actual_lakenum - k); i++){
		//cout << lakes[i].second << endl;
		summation += lakes[i].first;
		for(int row = 0; row < n; row++){
			for(int col = 0; col < m; col++){
				if(mp[row][col] == lakes[i].second){
					mp[row][col] = -2;
				}
			}
		}
	}
	cout << summation << endl;
	for(int row = 0; row < n; row++){
		for(int col = 0; col < m; col++){
			if(mp[row][col] == -2){
					cout << "*";
			} else {
					cout << ".";
			}
				
		}
		cout << endl;
	}
}