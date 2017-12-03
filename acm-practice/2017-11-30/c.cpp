#include<bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> sizes;
    for(int i = 0; i < n-1; i++){
        int a;
        cin >> a;
        sizes.push_back(a);
    }

    vector<double> lengths = {0.0};
    vector<double> widths; = {0.0};
    double length = 841.0;
    double width = 594.0;
    for(int i = 1; i < n; i++){
        lengths.push_back(length);
        widths.push_back(width);
        length = width/2;
        width = length * (841.0/594.0);
    }

    double ans = 0.0;
    for(int i = 0; i < n-1; i++){
        ans += length
    }
    return 0;
}