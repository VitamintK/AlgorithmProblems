#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <utility>
#include <map>
#include <set>
using namespace std;

int main(){
	long long n;
	cin >> n;
	long long mex = 0;
	long long a;
	long long as[100001];
	for(long long i = 0; i < n; i++){
		cin >> as[i];
}
sort(as, as+n);
for(long long i = 0; i < n; i++){
		if(as[i] >mex){
		   mex++;
		}	
	}
	cout << ++mex;
	return 0;
}
