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
	int n;
	cin >> n;
	bool in_p = false;
	bool was_letter = false;
	int cur_len = 0;
	int words = 0;
	int max_len_out = 0;
	char c;
	for(int i = 0; i < n; i++){
		cin >> c;
		if(c == '_'){
			if(in_p){
				if(was_letter){
					words++;
				}
			} else {
				max_len_out =max(max_len_out, cur_len);
			}
			cur_len = 0;
			was_letter = false;
		}
		else if(c == '('){
			in_p = true;
			max_len_out = max(max_len_out, cur_len);
			cur_len = 0;
			was_letter = false;
		}
		else if(c == ')'){
			if(was_letter){
					words++;
			}
			in_p = false;
			cur_len = 0;
			was_letter = false;
		}
		else {
			was_letter = true;
			cur_len++;
		}
	}
	max_len_out = max(max_len_out, cur_len);
	cout << max_len_out << " " << words;
}