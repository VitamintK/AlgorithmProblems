#include <iostream>
#include <vector>
#include <string>
#include <utility>
using namespace std;
int main(){
    //cout<<"started" << endl;
	int n, m, k;
	//cout << "first line works" << endl;
	int o, r, v;
	//cout << "second line works" << endl;
	scanf("%d", &n);
	//cout << n << endl;
	scanf("%d", &m);
	scanf("%d", &k);
			//cout <<"hdo" << endl;

	pair<int, int> rows[5001];
	pair<int, int> cols[5001];
			//cout <<"hso" << endl;

	for(int i = 1; i<k+1; i++){
		//cout <<"ho" << endl;
		scanf("%d%d%d", &o, &r, &v);
		//printf("%d %d %d\n", o, r, v);
		if(o == 1){
			rows[r-1] = make_pair(i, v);
		} else {
			cols[r-1] = make_pair(i, v);
		}
	}
	//cout << "helloe" << endl;
	for(int i = 0; i<n; i++){
		for(int j = 0; j<m; j++){
			printf("%d ", ((rows[i].first > cols[j].first) ? rows[i].second : cols[j].second));
		}
		printf("\n");
	}

	return 0;
}