#include <iostream>
#include <vector>
#include <string>
//TLE this is too naive
using namespace std;
int main(){
	int n, m, k;
	
	scanf("%d", &n);
	scanf("%d", &m);
	scanf("%d", &k);
	//cin >> m;
	//cin >> k;
	vector<vector<int> > v(n);
	for(int i = 0; i < n; i++){
		v[i].resize(m);
	}
	int o, r, c;
	for(int i = 0; i < k; i++){
	//	cin >>o;
	//	cin>>r;
	//	cin>>c;
		scanf("%d", &o);
	  scanf("%d", &r);
	  scanf("%d", &c);
		if(o == 1){
			for(int j = 0; j<m; j++){
				v[r-1][j] = c;
			}
		} else {
			for(int j = 0; j<n; j++){
				v[j][r-1] = c;
			}
		}
	}

	for(int i = 0; i<n; i++){
		for(int j = 0; j<m; j++){
			//cout << v[i][j] << " ";
			printf("%d ", v[i][j]);
		}
		printf("\n");
	}
	return 0;
}