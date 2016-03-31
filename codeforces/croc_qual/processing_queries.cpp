#include <iostream>
#include <deque>
#include <utility>
#include <vector>
using namespace std;
int main(){
	long n, b;
	scanf("%ld %ld", &n, &b);
	vector<pair<long, long> > queries;
	queries.reserve(n);
	deque<pair<long, long> > queueue;
	long real_values_queued = 0; 
	long start;
	long dur;
	long long end = 0;
	long processed = 0; //= the index to process
	for(long i = 0; i < n; i++){
		scanf("%ld %ld", &start, &dur);
		queries.push_back(make_pair(start, dur));
	}
	while(processed < n || queueue.size() > 0){
		while(queries[processed].first < end && processed < n){
			if(real_values_queued < b){
				queueue.push_back(queries[processed]);
				real_values_queued ++;
			} else {
				queueue.push_back(make_pair(-1, -1));
			}
			processed++;
		}
		pair<long, long> p;
		long long start;
		if(queueue.empty()){
			p = queries[processed];
			start = p.first;
			processed++;
		} else {
			p = queueue.front();
			queueue.pop_front();
			if(p.first != -1){
				real_values_queued--;
			}
			start = end;
		}
		if(p.first == -1){
			printf("-1 ");
		} else {
			printf("%I64d ", start + p.second);
			end = start + p.second;
		}
	}
	return 0;
}