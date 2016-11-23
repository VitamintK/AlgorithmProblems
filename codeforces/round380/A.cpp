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
#define ll long long
using namespace std;

int main(){
	ll n;
	cin >> n;
	string k;
	cin >> k;
	string p;
	bool in_ogo = false;
	ll i = 0;
	while(i < n){
		if(in_ogo){
			if(i+1 < n && k[i] == 'g' && k[i+1] == 'o'){
				i+=2;
				continue;
			} else {
				in_ogo = false;
			}
		} 
			if(i + 2 < n && k[i] == 'o' && k[i+1] == 'g' && k[i+2] == 'o'){
				in_ogo = true;
				p+="***";
				i+=3;
				continue;
			} else {
				p+= k[i];
				i++;
				continue;
			}
		
	}
	cout << p << endl;
	return 0;
}