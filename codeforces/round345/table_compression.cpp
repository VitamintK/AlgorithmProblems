#include<iostream>
#include<vector>
#include<utility>
using namespace std;

int main(){
	long n, m;
	scanf("%ld %ld", &n, &m);
	vector<vector<long> > grid(n);
	//long max_value = 0;
	//pair<long, long> max_pos;
	long num;
	for(long i = 0; i < n; i++){
		for(long j = 0; j < m; j++){
			scanf("%ld", &num);
			//if(num > max_value){
				//max_value = num;
				//max_pos = make_pair(i, j);
			//}
			grid[i].push_back()
		}
	}
	return 0;
}