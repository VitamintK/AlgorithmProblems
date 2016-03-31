#include <iostream>
#include <functional>
#include <string>
#include <unordered_map>
#include <utility>
#include <set>
#include <unordered_set>
using namespace std;
int main(){
	char a[3];
	char b[3];
	int aa;
	int bb;
	for(int i = 0; i < 3;){
		cin >> a[i]
		if(a[i] != 'X'){
						if(a[i] == 'A'){
				aa = i;
			}
			i++;

		}
	}
	for(int i = 0; i < 4;){
		cin >> b[i];
		if(b[i] != 'x'){
			if(b[i] == 'A'){
				bb = i;
			}
			i++;
		}
	}

	for(int i = 0; i < 3; i++){
		if(a[(aa+i)%3] != b[(bb+i)%3]){cout << "NO"; return 0;}
	}
	cout << "YES";
	return 0;
}