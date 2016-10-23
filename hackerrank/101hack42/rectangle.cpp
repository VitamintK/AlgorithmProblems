#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<set>
#include<utility>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int q;
    int n;
    cin >> q;
    for(int i = 0; i < q; i++){
        cin >> n;
        int x, y;
        set<int> xs;
        set<int> ys;
        vector<pair<int, int> > points;
        for(int j = 0; j < n; j++){
            cin >> x >> y;
            xs.insert(x);
            ys.insert(y);
            points.push_back(make_pair(x, y));
        }
        int minx = min(*xs.begin(), *(xs.begin()+1));
        int maxx = max(*xs.begin(), *(xs.begin()+1));
        int miny = min(*ys.begin(), *(ys.begin()+1));
        int maxy = max(*ys.begin(), *(ys.begin()+1));
        for(int j = 0; j < points.size(); j++){
            if(points[j].first < maxx && points[j].first > minx){
                if(points[j].second != miny && points[j].second != maxy){
                    cout << "NO" << endl;
                    break;
                }
            }
            if(points[j].second < maxy && points[j].second > miny){
                if(points[j].first != minx && points[j].first != maxx){
                    cout << "NO" << endl;
                    break;
                }
            } 
            if(j == points.size() -1){
                cout <<"YES" << endl;
            }
        }
    }
    return 0;
}
