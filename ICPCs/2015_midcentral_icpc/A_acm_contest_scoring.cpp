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
#include <unordered_map>

using namespace std;

int main(){
	int timescore = 0;
	int problems = 0;
	int min;
	char prob;
	string correct;
	cin >> min;
	int wrongs[26] = {0};
	while(min != -1){
		cin >> prob >> correct;
		if(correct == "right"){
			timescore += min + wrongs[prob-'A'];
			problems ++;
		} else {
			wrongs[prob-'A'] += 20;
		}
		cin >> min;
	}
	cout << problems << " " << timescore;
}