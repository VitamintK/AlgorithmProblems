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
	 ll id;
	 char poo;
	 ll num, denom;
	 for(ll i = 0; i < n; i++){
	 	cin >> id >> num >> poo >> denom;
	 	//cout << num << " " << denom << endl;
	 	ll ans = 1;
	 	ll addendium = 0;
	 	ll scalar = 1;
	 	while(denom != 1 || num != 1){
	 		if(num > denom){
	 			num -= denom;
	 			addendium+=scalar;
	 			scalar*=2;
	 		} else {
	 			denom-= num;
	 			scalar*=2;
	 		}
	 	}
	 	cout << id << " " << addendium+scalar << endl;
	 }
}