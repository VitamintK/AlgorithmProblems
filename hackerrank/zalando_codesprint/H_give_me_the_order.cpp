#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
//THIS IS 0(NM) which does not pass all the testcases.  A treap or some data structure that can do insert/delete or 
//moves on entire sections of elements in O(logn) is required.
int box_next[100001] = {0};
int box_prev[100001] = {0};
int box_id[100001] = {0};

int main() {
    ios::sync_with_stdio(false);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int N, M;
    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> box_id[i];
        box_next[i] = i+1;
        box_prev[i] = i-1;
    }
    box_next[N-1] = -1;
    int front = 0;
    cin >> M;
    int l, r;
    for(int i = 0; i < M; i++){
        cin >> l >> r;
        l--;
        r--;
        int trav = front;
        for(int a = 0; a < l; a++){
            trav = box_next[trav];
        }
        r = r - l;
        l = trav;
        for(int a = 0; a < r; a++){
            trav = box_next[trav];
        }
        r = trav;
        if(l != front){
            int prev = box_prev[l];
            int next = box_next[r];
            if(prev != -1){
                box_next[prev] = box_next[r];
            }
            if(next != -1){
                box_prev[next] = box_prev[l];
            }
                box_prev[front] = r;
                box_prev[l] = -1;

                box_next[r] = front;
                front = l;
        }
    }
    for(int i = front; i != -1; i = box_next[i]){
        cout << box_id[i] << " ";
    }
    return 0;
}
