#include <iostream>
using namespace std;
int main(){
	int n, m;
	int count = 0;
	scanf("%d %d", &n, &m);
	while(n != 0 && m != 0 && !(n<=1 && m<=1)){
		if(n > m){
			m++;
			n-=2;
		} else {
			n++;
			m-=2;
		}
		count++;
	}
	cout << count;
	return 0;
}