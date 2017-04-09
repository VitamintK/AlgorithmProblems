#include <stdio.h>
#include <math.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;
//ios::sync_with_stdio(false);

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int T;
    int B;
    long long M;
    cin >> T;
    int Bs[50][50];
    for(int t = 0; t < T; t++){
        cout << "Case #" << t+1 << ": ";
        //empty the graph
        for(int i = 0; i < 50; i++){
            for(int j = 0; j < 50; j++){
                Bs[i][j] = 0;
            }
        }
        cin >> B >> M;
        
        //if impossible
        if(M > pow(2, B-2)){
            cout << "IMPOSSIBLE" << endl;
            continue;
        } else {
            cout << "POSSIBLE" << endl;
        }
        //otherwise
        //find how many nodes besides B and 1 u'll need
        int extran = ceil(log2(M));
        //generate the full graph.
        for(int i = B-2; i>B-2 - extran; i--){
            for(int j = B-1; j>i; j--){
                Bs[i][j] = 1;
            }
        }
        //find what to cull.
        long long extrap = pow(2, extran) - M;
        //cout << "extrap is " << extrap << endl;
        //cout << "extran is " << extran << endl;
        int tst = 0; //tst represents 2^tst
        long long doineed;
        //add edges to the nodes that arent culled.
        Bs[0][B-1] = 1;
        while(tst < extran){
            if((extrap & 1) == 0){
                //cout <<"WE HERE WE MADE IT" << endl;
                Bs[0][B-2-tst] = 1;
            } //else { cout << extrap << endl;}
            tst++;
            extrap = extrap >> 1;
        }
        //print
        for(int x = 0; x < B; x++){
            for(int y = 0; y < B; y++){
                cout << Bs[x][y];
            }
            cout << endl;
        }

    }
    return 0;
}
