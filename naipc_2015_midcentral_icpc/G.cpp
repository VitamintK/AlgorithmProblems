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
	bool Ls[269000] = {0};
	long L;
	cin >> L;
	//long i = 0;
	//read input
	while(L != -1){
		Ls[L] = true;
		//i++;
		cin >> L;
	}
	//prestore how many bits are in each number up to 250001
	// int bits[263002];
	// for(long ii = 0; ii < 263002; ii++){
	// 	int bit = 0;
	// 	long k = ii;
	// 	while(k != 0){
	// 		bit++;
	// 		k &= k-1;
	// 	}
	// 	bits[ii] = bit;
	// }
	//O(n squared) compare all to get answer
	for(int wasdf= 0; wasdf < 250001; wasdf++){
		if(Ls[wasdf]){
			long ans = 0;
			for(int i = 0; i < 18; i++){
				for(int j = i; j < 18; j++){
					long alt = ((1 << i) | (1 << j)) ^ wasdf;
					//cout << alt << endl;
					if(Ls[alt] && alt > wasdf){
						//cout << alt << ", " << i << ", " << j << endl;
						ans++;
					}
				}
			}
			cout << wasdf << ":" << ans << endl;
		}
	}
	// 		if((bits[Ls[k] ^ Ls[j]] <= 2) && Ls[k] > Ls[j]){
	// 			ans++;
	// 		}
	// 	}
	// 	cout << Ls[j] << ":" << ans << endl;
	// }
}