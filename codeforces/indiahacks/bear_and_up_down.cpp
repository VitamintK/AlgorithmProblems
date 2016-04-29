#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
using namespace std;


int main(){
	long n;
	long t;
	long previous;
	cin >> n;
	vector<long> v;
	for(long i = 0; i < n; i++){
		cin >> t;
		v.push_back(t);
	}
	vector<long> bads;
	for(long i = 0; i < n; i++){
		if(i != 0 && i != n-1){
			if((v[i-1] > v[i]) == (v[i] > v[i+1])){
				bads.push_back()
			}
		}
	}
	return 0;
}