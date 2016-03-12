#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//getBestSubsequenceWithTail

int binarySearchLength(vector<pair<int, int> > subs, int value, bool insert){
	int r = subs.size() -1;
	int l = 0;
	int mid;
	while (r >= l){
		mid = (r + l) / 2;
		if (subs[mid].first == value){
			return mid;
		}
		if (subs[mid].first > value){
			r = mid - 1;
		}
		else{
			l = mid + 1;
		}
	}
	if (insert){
		return mid;
	}
	else{
		return -1;
	}
}


int main() {
	int t;
	int n;
	int globalLongest = 0;
	scanf("%d", &t);
	vector<pair<int, int> > subs;
	//first = length of subsequence; second = value of the last element of subsequence
	for (int i = 0; i < t; i++){
		scanf("%d", &n);
		//cout << n << endl;
		vector<pair<int, int> >::iterator longest = subs.begin();
		vector<pair<int, int> >::iterator shortest = subs.begin();
		
		bool n_is_smallest = true;
		for (vector<pair<int, int> >::iterator j = subs.begin(); j<subs.end(); j++){
			//cout << "here";
			//cout << longest->first << " is longest " << endl;
			if (j->first >= longest->first && j->second < n){
				//cout << "  " << longest->first << ", " << longest->second << endl;
				longest = j;
				n_is_smallest = false;
			}
			if (j->first < shortest->first){
				shortest = j;
			}
			if (j->second < n){
				n_is_smallest = false;
				//if(j ->first >= longest.first){
				//}
				//longest = make_pair(subs[j].first + 1, n);
			}
			//cout << longest.first << " " << longest.second << endl;
			//cout << subs[j].first << "--" << subs[j].second << endl;
		}
		if (n_is_smallest){
			//cout << "n is the smallest" << endl;
			if (!subs.empty()){
				subs[0] = make_pair(1,n);
			} else {
			//cout << shortest->first << shortest->second<<endl;
			subs.insert(subs.begin(), make_pair(1, n));
            }
			//cout << shortest->first << shortest->second;
		}
		else {
			pair<int, int> temp = make_pair(longest->first + 1, n);
			
			globalLongest = max(temp.first, globalLongest);
			int index_to_erase = binarySearchLength(subs, temp.first, false);
			if (index_to_erase > -1){
				//cout << "Erasing " << index_to_erase << endl;
				subs[index_to_erase] = temp;
			} else {
			subs.insert(subs.begin() + binarySearchLength(subs, temp.first, true) + 1, temp);
            }
			//cout << temp.first << endl;

		}
		//subs.push_back(longest);
		//cout << "asdf" << endl;
	}
	printf("%d", globalLongest);
	return 0;
}
