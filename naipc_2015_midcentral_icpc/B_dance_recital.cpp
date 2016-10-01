#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std; 

const int maxn = 20;
string recitals[maxn]; 

int changes[maxn][maxn];

int qChange(int i, int j){
	if(changes[i][j] != -1)
		return changes[i][j];

	string a = recitals[i];
	string b = recitals[j];

	int A[26] = {0},B[26]={0};
	for(int i=0;i<a.length();i++)
		A[a[i]-'A']++;
	for(int i=0;i<b.length();i++)
		B[b[i] - 'A']++;

	int c = 0;
	for(int i=0;i<26;i++)
		if(A[i] && B[i])
			c++;
	changes[i][j] = c;

	//cout << a << " " << b << " " << c << endl;

	return c;
}
int main(){

	int R;
	cin >> R;

	std::vector<int> order;
	for(int i=0;i<R;i++){
		cin >> recitals[i];
		order.push_back(i);
	}

	for(int i=0;i<maxn;i++)
		for(int j=0;j<maxn;j++)
			changes[i][j] = -1;

	int ans = -1;
	do{
		int cur = 0;
		for(int i=1;i<R;i++){
			cur += qChange(order[i-1], order[i]);
		}
		if(ans == -1 || cur < ans)
			ans = cur;

	}
	while(std::next_permutation(order.begin(), order.end()));


	cout << ans << endl;
	return 0;
}