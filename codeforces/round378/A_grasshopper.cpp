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
	string s;
	cin >> s;
	int maxlength = 0;
	int curlength = 0;
	for(int i = 0; i < s.length(); i++){
		curlength++;
		if(s[i] == 'A' || s[i] == 'E'|| s[i] == 'I'|| s[i] == 'O'|| s[i] == 'U' || s[i] == 'Y'){
			maxlength = max(maxlength, curlength);
			curlength = 0;
		}
	}
	curlength++;
	maxlength = max(maxlength, curlength);
	cout << maxlength << endl;
}