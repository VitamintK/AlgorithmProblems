#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

struct chuteladder{
    int start;
    int end;
};

int main() {
    int n;
    int m;
    cin >> n;
    char temp;
    char* board = new char[n*n];
    map<char, chuteladder> chutes;
    for(int row = 0; row<n; ++row){
        for(int col = 0; col < n; col++){
            cin >> temp;
            //cout << temp << " "; 
            if(row%2 == 0){
                board[(n-1-row) * n + col] = temp;
            } else {
                board[(n-1-row) * n + (n-1-col)] = temp;
            }
        }
    }
    
    for(int REMOVETHIS=0;REMOVETHIS<n*n;REMOVETHIS++){
        //cout << board[REMOVETHIS] << endl;
        temp = board[REMOVETHIS];
        if(temp != '-'){
                if(chutes.find(temp) == chutes.end()){
                    chutes[temp] = *new chuteladder;
                    if(isdigit(temp)){
                        chutes[temp].start = REMOVETHIS;
                        //cout << chutes[temp].start << "????" << REMOVETHIS << endl;
                    }
                    else {
                        chutes[temp].end = REMOVETHIS;
                    }
                }
                else {
                    if(isdigit(temp)){
                        chutes[temp].end = REMOVETHIS;
                    }
                    else {
                        chutes[temp].start = REMOVETHIS;
                        //cout << chutes[temp].start << ")()()" << REMOVETHIS << endl;
                    }
                }
            }
    }
    cin >> m;
    int evil = 0;
    int* players = new int[m]();
    for(int zoo = 0; zoo < m; zoo++){
        players[zoo] = -1;
    }
    int turnplayer = 0;
    int last_roll = 0;
    int move;
    int rolls_to_go = 2;
    bool stop = false;
    bool chuted = true;
    while(cin >> move){
        //cout << move << endl;
        rolls_to_go--;
        players[turnplayer] += move;
        if(rolls_to_go == 0){
            //this is the final location of the dice rolls.
            //now calculate whether to leapfrog another player or move up a chute/ladder
            set<int> moved;
            chuted = true;
            stop = false;
            while(chuted == true && evil == 0){
                //cout << "I'M HERE" << endl;
                for(set<int>::iterator i = moved.begin(); i != moved.end(); i++){
                //    cout << "!" << *i << endl;
                }
                chuted = false;
                stop = false;
                while(stop == false){
                    //cout << "Line 89" << endl;
                    //cout << "DUde's at " << players[turnplayer] << endl;
                    stop = true;
                    for(int player = 0;player<m;player++){
                        if((player != turnplayer) && (players[player] == players[turnplayer])){
                            players[turnplayer]++;
                            //cout << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;
                            if(moved.count(players[turnplayer]) == 1){
                                evil = turnplayer + 1;
                                stop = true;
                            } else {
                                moved.insert(players[turnplayer]);
                                //cout << "hi i am here now" << endl;
                                stop = false;
                            }
                        }
                    }
                }
                //cout <<"now dude's at " << players[turnplayer] << endl;
                if(evil == 0 && board[players[turnplayer]] != '-'){
                    //cout << "ok now i am hereeeee" << endl;
                    if(players[turnplayer] == chutes[board[players[turnplayer]]].start){
                        players[turnplayer] = chutes[board[players[turnplayer]]].end;
                        if(moved.count(players[turnplayer]) == 1){
                            evil = turnplayer + 1;
                        } else {
                            moved.insert(players[turnplayer]);
                            chuted = true;
                        }
                    }
                }
            }
            //cout << turnplayer << ": " << players[turnplayer] << endl;
            if(evil > 0){
                cout << "PLAYER " << evil << " WINS BY EVIL CYCLE!" << endl;
                return 0;
            }
            if(move == last_roll){
                //rolled doubles
                rolls_to_go = 1;
                last_roll = 0;
            }
            else {
                //did not roll doubles
                rolls_to_go = 2;
                last_roll = 0;
                turnplayer = ((turnplayer+1)%m);
            }
        } else {
            last_roll = move;
        }
    }
    //cout << "hi";
    for(int j=0;j<m;j++){
        cout << min(players[j]+1, n*n) << " ";
    }
    return 0;
}
