#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int a, c, b;
    cin >> a >> b >> c;
    pair<int, char> smallest[3];
    smallest[0].first = a;
    smallest[0].second = 'A';
    smallest[1].first = b;
    smallest[1].second = 'B';
    smallest[2].first = c;
    smallest[2].second = 'C';
    sort(smallest, smallest+3);
    reverse(smallest, smallest+3);
    for(int i = 0; i < 3; i++){
        if(smallest[i].second == 'A')
            a = i;
        if (smallest[i].second == 'B')
            b = i;
        if (smallest[i].second == 'C')
            c = i;
    }
    //cout << a << " " << b << " " << c << endl;
    int N;
    cin >> N;
    string p;
    int rep;
    int reps[8] = {0};
    for(int i = 0; i < N; i++){
        cin >> p;
        rep = 0;
        for(char j : p){
            if(j == 'A'){
                rep |= (int)pow(2,a);
            }
            else if(j == 'B'){
                rep |= (int)pow(2,b);
            } else if(j == 'C'){
                rep |= (int)pow(2,c);
            }
        }
        reps[rep]++;
    }
    int ans = 0;
    bool quit = false;
    for(int i = 0; i < 8; i++){
        quit = false;
        for(int j = 0; j<reps[i]; j++){
            for(int bin = 0; bin < 3; bin++){
                if((i >> bin)&1){
                    smallest[bin].first--;
                    if(smallest[bin].first < 0){
                        //cout << ans;
                        //return 0;
                        for(int bin2 = 0; bin2 <=bin; bin2++){
                            if((i >> bin2)&1){
                                smallest[bin2].first++;
                            }
                        }
                        quit = true;
                        break;
                    }
                }
            }
            if(quit){
                break;
            }
            ans++;
        }
    }
    cout << ans;
    return 0;
}
