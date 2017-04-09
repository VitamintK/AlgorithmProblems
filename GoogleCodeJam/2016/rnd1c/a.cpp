
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;
//ios::sync_with_stdio(false);

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
  long long T;
  long long N;
  long long Ps[26];
  cin >> T;
  for(long long i = 0; i < T; i++){
    cout << "Case #" << i+1 << ": ";
    bool parity = true;
    long total = 0;
    cin >> N;
    for(int j = 0; j < N; j++){
        cin >> Ps[j];
        total+= Ps[j];
    }
    if(total%2 == 1){
        int maxi = 0;
        int maxin = -1;
        for(int k = 0; k<N; k++){
            if(Ps[k] > maxi){
                maxi = Ps[k];
                maxin = k;
            }
        }
        Ps[maxin]--;
        cout << (char)('A' + maxin) << " ";
    }
    while(true){
        int maxi = 0;
        int maxin = -1;
        for(int k = 0; k<N; k++){
            if(Ps[k] > maxi){
                maxi = Ps[k];
                maxin = k;
            }
        }
        if(maxin == -1){
            break;
        }
        Ps[maxin]--;
        cout << (char)('A' + maxin);
        parity = !parity;
        if(parity){
            cout << " ";
        }
    }
    cout << endl;
  }
    return 0;
}
