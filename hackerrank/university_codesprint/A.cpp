#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#define ll long long
using namespace std;


int main(){
    ll a;
    ll b;
    ll c;
    ll d;
    ll e;
    cin >> a >> b >> c >> d >> e;
    ll summ = a+b+c+d+e;
    cout << summ - max({a,b,c,d,e}) << " " << summ-min({a,b,c,d,e}) << endl;
    return 0;
}
