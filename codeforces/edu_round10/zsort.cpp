#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;


int main(){
	vector<long long> asc;
	//vector<long long> des(1000);
	int n;
	cin >> n;
	long long k;
	for(int i = 0; i < n; i++){
		cin >> k;
		asc.push_back(k);
	}
	//cout << asc[1];
	sort(asc.begin(), asc.end());
	//cout << asc[1];
	vector<long long> des = asc;
	//cout << asc[1];
	reverse(des.begin(), des.end());
	bool small = true;
	for(int i = 0; i < n; i++){
		if(small){
			cout << asc[i/2] << " ";
		} else {
			cout << des[i/2] << " ";
		}
		small = !small;
	}

	return 0;
}