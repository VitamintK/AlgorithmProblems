#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define PI 3.14159265

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int W, H, N;
    int w, h;
    char t;
    cin >> W>>H>>N;
    for(int i = 0; i < N; i++){
        cin >> t;
        if(t == 'C'){
            cin >> w;
            w = w*2;
            if(w <= W && w <=H){
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }
        } else {
            cin >> w >> h;
            float  x, y;
            bool flag = false;
            for(float ang = 0.0; ang > -0.5; ang-=0.001){
                x = cos(PI*ang)*w - sin(PI*ang)*h;
                y = cos(PI*ang)*h - sin(PI*ang)*w ;
                //cout << x << " " << y << endl;
                if((x<=W && y<=H) || (x<=H && y <= W)){
                    cout << "YES" << endl;
                    flag = true;
                    break;
                }
            }
           // if((w <= W && h <= H) || (w <= H && h <= W) || sqrt(w*w + h*h) < h){
           //     cout << "YES" << endl;
           // } else {
            if(!flag){
                cout << "NO" << endl;
            }
           // }
        }
    }
    return 0;
}
