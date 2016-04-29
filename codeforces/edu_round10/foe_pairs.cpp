#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

const int Maxn = 300010;
long long a[Maxn], w[Maxn], b[Maxn];
int n,m;
int main(){
	cin >> n>>m;
	for(long i = 1; i <= n; i++){
		cin >> a[i];
		b[a[i]] = i;
	}
	long long x, y;
	for(int i=1;i<=n;i++){
		cin >> x >> y;
		x = b[x];
		y = b[y];
		if (x > y) swap(x,y);
		w[y] = max(w[y],x);
	}
	long long ans = 0, now = 1;
	for (int i=1;i<=n;i++){
		now = max(now, w[i]);
		ans += i - now + 1;
	}
	cout << ans << endl;

	return 0;
}