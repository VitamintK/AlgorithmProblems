#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;


int lis2() {
	int t;
	int n;
	int globalLongest = 0;
	scanf_s("%d", &t);
	map<int, int> subs;
	//first = length of subsequence; second = value of the last element of subsequence
	for (int i = 0; i < t; i++){
		scanf_s("%d", &n);
		bool n_is_smallest = true;
		for (map<int, int>::iterator i = subs.begin(); i != subs.end(); i++){
			//cout << "here";
			cout << longest->first << " is longest " << endl;
			if (j->first >= longest->first && j->second < n){
				cout << "  " << longest->first << ", " << longest->second << endl;
				longest = j;
				n_is_smallest = false;
			}
			if (j->first < shortest->first){
				shortest = j;
			}
			if (j->second < n){
				n_is_smallest = false;
			}
		}
		if (n_is_smallest){
			cout << "n is the smallest" << endl;
			if (!subs.empty()){
				subs.erase(shortest);
			}
			//cout << shortest->first << shortest->second<<endl;
			subs.insert(subs.begin(), make_pair(1, n));
			//cout << shortest->first << shortest->second;
		}
		else {
			pair<int, int> temp = make_pair(longest->first + 1, n);
			
			globalLongest = max(temp.first, globalLongest);
			int index_to_erase = binarySearchLength(subs, temp.first, false);
			if (index_to_erase > -1){
				cout << "Erasing " << index_to_erase << endl;
				subs.erase(subs.begin() + index_to_erase);
			}
			subs.insert(subs.begin() + binarySearchLength(subs, temp.first, true) + 1, temp);
			cout << temp.first << endl;

		}
		//subs.push_back(longest);
		//cout << "asdf" << endl;
	}
	printf("%d", globalLongest);
	return 0;
}
