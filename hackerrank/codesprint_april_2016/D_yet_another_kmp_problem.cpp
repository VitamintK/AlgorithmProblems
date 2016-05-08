#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    long letters[26];
    int min_letter;
    int first_letter = 27;
    long min_quant = 1000001;
    char ans[1000000];
    for(int i = 0; i < 26; i++){
        cin >> letters[i];
        if(letters[i] > 0 && first_letter == 27){
            first_letter = i;
        }
        if(letters[i] < min_quant && letters[i] > 0){
            min_quant = letters[i];
            min_letter = i;
        }
    }
    
    if(first_letter == min_letter && letters[first_letter] > 1){
        ans[0] = (char)(min_letter+97);
        //cout << min_letter << endl;
        
        ans[1] = (char)(min_letter+97);
        long i = 1;
        bool just_min = true;
        letters[min_letter]-=2;
        for(int j = min_letter+1; j < 26; j++){
            for(long k = 0; k < letters[j];){
                if(just_min == false && letters[min_letter] > 0){
                    ans[++i] = (char)(min_letter+97);
                    letters[min_letter]--;
                    just_min = true;
                } else {
                    just_min = false;
                    ans[++i] = (char)(j+97);
                    k++;
                }
            }
        }
        while(letters[min_letter] > 0){
            ans[++i] = (char)(min_letter+97);
            letters[min_letter]--;
        }
        ans[++i] = '\0';
    } else {
        ans[0] = (char)(min_letter+97);
        letters[min_letter]--;
        long i = 0;
        for(int j = 0; j < 26; j++){
            for(long k = 0; k < letters[j]; k++){
                ans[++i] = (char)(j+97);
            }
        }
        ans[++i] = '\0';
    }
    if(first_letter == 27){
        cout << "" << endl;
    } else {
    cout << ans << endl;
    }
    return 0;
}
