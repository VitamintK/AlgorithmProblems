#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <set>
#include <queue>
#include <utility>
#define ll long long
using namespace std;
//i hate this problem honestly roflmao
//ll dpf(ll row, ll col, int stuff){
//	bool is_king = (bool)(stuff&(1<<16));

//}
int countbits(int a){
	int ans = 0;
	while(a != 0){
		ans+= (a&1);
		a>>=1;
	}
	return ans;
}

int main(){
	ll t;
	cin >> t;
	int board[8][8] = {0};
	char piece;
	for(ll i = 0; i < t; i++){
		ll count = 0;
		ll row0, col0;
		bool is_king = false;
		for(ll row = 0; row < 8; row++){
			for(ll col = 0; col < 8; col++){
				cin >> piece;
				if(piece == 'o'){
					row0 = row;
					col0 = col;
					if(row0 == 0){
						is_king = true;
					}
				} else if(piece =='x'){
					board[row][col] = count;
					count++;
				}
			}
		}

		//ll dp[8][8][131073][4] = {0};
		vector<vector<vector<vector<ll>>>> dp(8,vector<vector<vector<ll>>>(8,vector<vector<ll>>(131073,vector<ll>(4,0))));
		//cout << ((1<<(count))-1 & (((1<<15)-1) | ((int)is_king)<<16)) << endl;
 		dp[row0][col0][(1<<(count))-1 & (((1<<15)-1) | ((int)is_king)<<16)][0] = 1; //up //honestly fuck this problem
 		dp[row0][col0][(1<<(count))-1 & (((1<<15)-1) | ((int)is_king)<<16)][1] = 1; //right
 		dp[row0][col0][(1<<(count))-1 & (((1<<15)-1) | ((int)is_king)<<16)][2] = 1; //down
 		dp[row0][col0][(1<<(count))-1 & (((1<<15)-1) | ((int)is_king)<<16)][3] = 1; //left
 		ll answer = 0;
		for(int pieces_lost = 0; pieces_lost <= count; pieces_lost++){
			for(int bitstuff = 0; bitstuff <  (1<<count); bitstuff++){
				if(count- countbits(bitstuff)==pieces_lost){
					for(bool king = false; king != true; king=true){
						int newbits = bitstuff | ((int)king << 16);
						for(ll row = 0; row < 8; row++){
							for(ll col = 0; col < 8; col++){
								if(dp[row][col][newbits][0]+dp[row][col][newbits][1]+dp[row][col][newbits][2]+dp[row][col][newbits][3] > 0){
									if((newbits&((1<<count)-1))^(((1<<count)-1)) == 0){//wow this logic is a little spurious
										answer+=dp[row][col][newbits][0]+dp[row][col][newbits][1]+dp[row][col][newbits][2]+dp[row][col][newbits][3];
									}
									if(king == false){
										if(col < 6 && board[row][col+1] !=0){ //going right
											int ncol = col+2;
											if(pieces_lost == 0){
														dp[row][ncol][newbits ^ (1<<board[row][ncol-1])][0]+=dp[row][col][newbits][0];
											} else { //if it times out then precompute the bit shift here
														dp[row][ncol][newbits ^ (1<<board[row][ncol-1])][0]+=dp[row][col][newbits][0];
														dp[row][ncol][newbits ^ (1<<board[row][ncol-1])][0]+=dp[row][col][newbits][1];
														dp[row][ncol][newbits ^ (1<<board[row][ncol-1])][0]+=dp[row][col][newbits][2];
											}
										}
										if(col > 1 && board[row][col-1] != 0){ //going left
											int ncol = col-2;
											if(pieces_lost == 0){
														dp[row][ncol][newbits ^ (1<<board[row][ncol+1])][0]+=dp[row][col][newbits][0];
													} else { //if it times out then precompute the bit shift here
														dp[row][ncol][newbits ^ (1<<board[row][ncol+1])][0]+=dp[row][col][newbits][0];
														dp[row][ncol][newbits ^ (1<<board[row][ncol+1])][0]+=dp[row][col][newbits][2];
														dp[row][ncol][newbits ^ (1<<board[row][ncol+1])][0]+=dp[row][col][newbits][3];
													}
										}
										if(row > 1 && board[row-1][col] != 0){ //going up
											int nrow = row-1;
											if(pieces_lost == 0){
														dp[nrow-1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][0];
													} else { //if it times out then precompute the bit shift here
														dp[nrow-1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][0];
														dp[nrow-1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][1];
														dp[nrow-1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][3];
													}
										}
										if(row < 6 && board[row+1][col] != 0){//i dont know what i'm typing anymore
											//going down like my life
											int nrow = row+1;
												if(pieces_lost == 0){
														dp[nrow+1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][0];
													} else { //if it times out then precompute the bit shift here
														dp[nrow+1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][1];
														dp[nrow+1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][2];
														dp[nrow+1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][3];
													}
										}
										break;
									}
									//let's go RIGHT!
										ll ncol = col;
										bool seen_real_enemy = false;
										int enemy_killed;
										while(ncol < 7){
											if(board[row][ncol] != 0 && (newbits & (1<<board[row][ncol]))){
												//following logic is iffy.  debug this first.
												if(seen_real_enemy){
													break;
												} else {
													seen_real_enemy = true;
													enemy_killed = board[row][ncol];
													if(pieces_lost == 0){
														dp[row][ncol+1][newbits ^ (1<<board[row][ncol])][0]+=dp[row][col][newbits][0];
													} else { //if it times out then precompute the bit shift here
														dp[row][ncol+1][newbits ^ (1<<board[row][ncol])][0]+=dp[row][col][newbits][0];
														dp[row][ncol+1][newbits ^ (1<<board[row][ncol])][0]+=dp[row][col][newbits][1];
														dp[row][ncol+1][newbits ^ (1<<board[row][ncol])][0]+=dp[row][col][newbits][2];
													}
												}
											} else {
												if(seen_real_enemy){
													if(pieces_lost == 0){
														dp[row][ncol+1][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][0];
													} else {
														dp[row][ncol+1][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][0];
														dp[row][ncol+1][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][1];
														dp[row][ncol+1][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][2];
													}
												}
											}
											ncol++;
										}
									//GO LEFT
										 ncol = col;
										seen_real_enemy = false;
										enemy_killed;
										while(ncol >= 1){
											if(board[row][ncol] != 0 && (newbits & (1<<board[row][ncol]))){
												//following logic is iffy.  debug this first.
												if(seen_real_enemy){
													break;
												} else {
													seen_real_enemy = true;
													enemy_killed = board[row][ncol];
													if(pieces_lost == 0){
														dp[row][ncol-1][newbits ^ (1<<board[row][ncol])][0]+=dp[row][col][newbits][0];
													} else { //if it times out then precompute the bit shift here
														dp[row][ncol-1][newbits ^ (1<<board[row][ncol])][0]+=dp[row][col][newbits][0];
														dp[row][ncol-1][newbits ^ (1<<board[row][ncol])][0]+=dp[row][col][newbits][2];
														dp[row][ncol-1][newbits ^ (1<<board[row][ncol])][0]+=dp[row][col][newbits][3];
													}
												}
											} else {
												if(seen_real_enemy){
													if(pieces_lost == 0){
														dp[row][ncol-1][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][0];
													} else {
														dp[row][ncol-1][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][0];
														dp[row][ncol-1][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][2];
														dp[row][ncol-1][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][3];
													}
												}
											}
											ncol--;
										}
									//row check king make king do king jk already king ha ha
										//LETS GO UP
										ll nrow = row;
										seen_real_enemy = false;
										enemy_killed;
										while(nrow >= 1){
											if(board[nrow][col] != 0 && (newbits & (1<<board[nrow][col]))){
												//following logic is iffy.  debug this first.
												if(seen_real_enemy){
													break;
												} else {
													seen_real_enemy = true;
													enemy_killed = board[nrow][col];
													if(pieces_lost == 0){
														dp[nrow-1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][0];
													} else { //if it times out then precompute the bit shift here
														dp[nrow-1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][0];
														dp[nrow-1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][1];
														dp[nrow-1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][3];
													}
												}
											} else {
												if(seen_real_enemy){
													if(pieces_lost == 0){
														dp[nrow-1][col][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][0];
													} else {
														dp[nrow-1][col][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][0];
														dp[nrow-1][col][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][1];
														dp[nrow-1][col][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][3];
													}
												}
											}
											nrow--;
										}
									//LETS GO DOWN
										 nrow = row;
										seen_real_enemy = false;
										enemy_killed;
										while(nrow < 7){
											if(board[nrow][col] != 0 && (newbits & (1<<board[nrow][col]))){
												//following logic is iffy.  debug this first.
												if(seen_real_enemy){
													break;
												} else {
													seen_real_enemy = true;
													enemy_killed = board[nrow][col];
													if(pieces_lost == 0){
														dp[nrow+1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][0];
													} else { //if it times out then precompute the bit shift here
														dp[nrow+1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][1];
														dp[nrow+1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][2];
														dp[nrow+1][col][newbits ^ (1<<board[nrow][col])][0]+=dp[row][col][newbits][3];
													}
												}
											} else {
												if(seen_real_enemy){
													if(pieces_lost == 0){
														dp[nrow+1][col][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][0];
													} else {
														dp[nrow+1][col][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][1];
														dp[nrow+1][col][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][2];
														dp[nrow+1][col][newbits ^ (1<<enemy_killed)][0]+=dp[row][col][newbits][3];
													}
												}
											}
											nrow++;
										}
								}
							}
						}
					}
				}
			}
		}
		cout << answer << endl;
	}
}