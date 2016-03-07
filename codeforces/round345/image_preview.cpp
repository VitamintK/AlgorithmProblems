//goddamn this is naive
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <utility>
using namespace std;
int compute_travel(int front, int back, int a){
	if(front == 0 || back == 0){
		return 0;
	} else {
		return (min(front,back))*a;
	}
}
int main(){
	int n, a, b;
	long T;
	scanf("%d %d %d %ld\n", &n, &a, &b, &T);
	vector<long> forwards; //represents the cost to go from 1 to including n
	char orient;
	int cost;
	long total_cost = 0;
	for(int i = 0; i < n; i++){
		scanf("%c", &orient);
		//cout << orient << endl;
		cost = 1 + a;
		if(i == 0){
			cost -=a;
		}
		if(orient == 'w'){
			cost+= b;
		}
		total_cost+=cost;
		//cout << total_cost << " ";
		forwards.push_back(total_cost);
	}
	//cout <<endl;
	long max_back = n-1;
	long most_photos = 0;
	for(int i = 0; i<n; i++){
		//i is the i_th index that we've included going from the front.  it is at least 0.
		//                              #of backs used+#fronts used*cost of swipe
		while(max_back + i >= n){
			max_back--;
		}
		while(max_back > 0 && (compute_travel(i,(max_back),a) + total_cost - forwards[n-1-max_back] + forwards[i] > T)){
			//max_back is how many we've used from the back.
			max_back--;
				//cout <<i << " " << max_back << endl;

		}
		if(compute_travel(i,(max_back),a) + total_cost - forwards[n-1-max_back] + forwards[i] <= T){
		    //cout << i << " " << max_back << " " << compute_travel(i,(max_back),a) + total_cost - forwards[n-1-max_back] + forwards[i] << endl;
		    most_photos = max(most_photos, max_back+i+1);
		}
	}
	cout << most_photos << endl;
	return 0;
}