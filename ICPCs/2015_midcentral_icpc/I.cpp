#include<iostream>
using namespace std;

const int maxn = 5010;

int w[maxn], h[maxn];
int n, c;

int d[maxn][maxn];

const int inf = 1<<29;

int main(){

    cin >> n >> c;
    for(int i=0;i<n;i++)
        cin >> w[i] >> h[i];

    for(int i=0;i<n;i++)
        d[i][i] = h[i];
    
    for(int diag=1; diag <n; diag++){
        for(int i=0; i+diag <n; i++){
            int j = i + diag;
            // Find d[i][j]
            d[i][j] = inf;
            int max_height = 0;
            int sum_width = 0;

            for(int k=i; k <= j; k++){
                max_height = max(max_height, h[k]);
                sum_width += w[k];
                if(sum_width > c)
                    break;
                
                d[i][j] = min(d[i][j], max_height + d[k+1][j]);
            }
        }
    }

    //for(int i=0;i<n;i++){
        //for(int j=0;j<n;j++)
        //    cout << d[i][j] << "\t";
      //  cout << endl;
    //}

    cout << d[0][n-1] << endl;
    return 0;
}