#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
//ios::sync_with_stdio(false);

struct tree{
    vector<tree*> children;
    tree * parent;
    bool right = false;
}root;

int main() {
    tree * asdf[500000];
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    long n, m, p;
    cin >> n >> m >> p;
    string str;
    cin >> str;
    string seq;
    cin >> seq;
    tree* focus = &root;
    tree* cursor;
    for(long i = 0; i < n; i++){
        if(str[i] == '('){
            tree newch = new tree;
            newch.parent = focus;
            //*focus.children.push_back(tree )
            focus->children.push_back(&newch);
            focus = &newch;
        } else {
            focus = focus->parent;
        }
        //asdf[i] = focus;
    }



    return 0;
}
