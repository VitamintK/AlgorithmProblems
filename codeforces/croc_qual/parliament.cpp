#include <iostream>
using namespace std;
int main(){
	long n, a, b;
	scanf("%ld %ld %ld", &n, &b, &a);
	if(n > a*b){
		printf("%d", -1);
	} else {
		bool parity_odd = true;
		long even = 2;
		long odd = 1;
		long num_to_print;
		for(int i = 0; i < b; i++){
			for(int j = 0; j < a; j++){
				if(parity_odd){
					if(odd <= n){
					num_to_print = odd;
					odd+=2;
					} else {
						num_to_print = 0;
					}
				}else{
					if(even <=n){
					num_to_print = even;
					even+=2;
					} else {
					num_to_print = 0;
					}
				}
				printf("%d", num_to_print);
				parity_odd = !parity_odd;
				if(j != a-1){printf(" ");}
			}
			if(a%2 == 0){parity_odd = !parity_odd;}
			if(i != b-1){printf("\n");}
		}
	}
}