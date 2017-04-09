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
int ord[1000];
int a;
int s;

int binary_search(int search,int patel[], int lower, int upper){
	int mid = (lower +upper)/2;
	cout << "lower: " << lower  << "upper: " << upper << "mid: " <<mid << endl; 
	if(patel[mid] == search){
		return mid;

	}
	else{
	if (mid == lower || mid == upper){
		return 1234;
	}
		else{ 
		if(patel[mid] > search){
			upper = mid;
			return binary_search(search, patel, lower, upper);
		}
		else{
			lower= mid;
			return binary_search(search, patel, lower, upper);
		}


		}
	}
	


}



int main(){
	cin >> n;
	cin >> s;
	for(int i =0; i<n; i++){
		cin >> ord[i];
	}

	cout << binary_search(s, ord, 0, n) <<endl;

	}

