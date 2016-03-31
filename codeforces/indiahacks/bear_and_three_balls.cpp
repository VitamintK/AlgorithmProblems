#include <iostream>
#include <vector>
using namespace std;
int main(){
	int k;
	cin >> k;
	vector<int> r(1001, 0);
	int l;
	for(int i = 0; i < k; i++){
		cin >> l;
		r[l] = 1;
	}
	int count = 0;
	for(int i = 1; i < 1001; i++){
		if(r[i] == 1){
			count++;
		} else {
			count = 0;
		}
		if(count == 3){
			cout << "YES" << endl;
			return 0;
		}
	}
	cout << "NO" << endl;
	return 0;
}