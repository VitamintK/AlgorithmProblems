#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <utility>
#include <map>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<pair<int, int>> v;
    int T;
    int M;
    int N;
    int a;
    int b;
    cin >> T;
    for(int i = 0; i<T; i++){
        cin >> M;
        cin >> N;
        map<int,int> min_distances; //maps the positions of robots to the min distance
        int old_b;
        for(int j = 0; j<N; j++){
            cin >> a;
            cin >> b;
            //cout << a << "," << b << endl;
            if(min_distances.size() == 0){
                min_distances[-1] = abs(b - a);
            } else {
                map<int, int> min_distances_new;
                int move_old_oth_dist;
                for(const auto& i: min_distances){
                    if(min_distances_new.count(i.first)==1){
                        min_distances_new[i.first] = min(min_distances_new[i.first], i.second + abs(b-a) + abs(a-old_b));
                    } else {
                        min_distances_new[i.first] = i.second + abs(b-a) + abs(a-old_b) ;
                    }
                    if(i.first == -1){
                        move_old_oth_dist = i.second + abs(b-a);
                    } else {
                        move_old_oth_dist = i.second + abs(i.first - a) + abs(b - a);
                    }
                    if(min_distances_new.count(old_b) == 1){
                       min_distances_new[old_b] = min(move_old_oth_dist, min_distances_new[old_b]);
                    } else {
                       min_distances_new[old_b] = move_old_oth_dist;
                    }
                    //cout << i.first << ": "<< min_distances_new[i.first] << ", ";
                    //cout << old_b << ": " << min_distances_new[old_b] << endl;
                    
                }
                min_distances = min_distances_new;
            }
            old_b = b;
        }
        int min_distance = 1000002;
        for(const auto& i: min_distances){
            min_distance = min(min_distance, i.second);
        }
        cout << min_distance << endl;
    }
    return 0;
}
