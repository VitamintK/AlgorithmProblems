#include<iostream>
#include <vector>
#include <utility>
using namespace std;
int main(){
	int n, m;
	long d;
	char c;
	scanf("%d %d", &n, &m);
	vector< pair<long, char> > t;
	vector<pair<long, char> > s;
	for(int i = 0; i < n; i++){
		scanf("%ld-%c", &d, &c);
		t.push_back(make_pair(d, c));
	}
	for(unsigned int i = 0; i < m; i++){
		scanf("%ld-%c", &d, &c);
		s.push_back(make_pair(d, c));
	}

	char last = t[0].second;
	for(unsigned int i = 1; i<t.size(); i++){
		if(t[i].second == last){
			t[i-1].first += t[i].first;
			t.erase(t.begin()+i);
			i--;
		} else {
			last = t[i].second;
		}
	}

	last = s[0].second;
	for(unsigned int i = 1; i<s.size(); i++){
		if(s[i].second == last){
			s[i-1].first += s[i].first;
			s.erase(s.begin()+i);
			i--;
		} else {
			last = s[i].second;
		}
	}

	long long int ans = 0;
	if(s.size() == 1){
		for(unsigned int i = 0; i < t.size(); i++){
			if(t[i].second == s[0].second && t[i].first >= s[0].first){
				ans+= 1 + t[i].first - s[0].first;
			}
		}
	} else {
		for(int i = 0; i < t.size(); i++){
			for(int j = 0; j< s.size(); j++){
				if(j == 0 || j == s.size()-1){
					if(s[j].second != t[i+j].second){
						break;
					}
					if(j == s.size()-1){
						ans++;
					}
				} else {
					if(s[j].second != t[i+j].second || s[j].first != t[i+j].first){
						break;
					}
				}
			}
		}
	}
	printf("%lld", ans);
	return 0;
}