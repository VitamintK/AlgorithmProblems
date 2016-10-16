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

using namespace std;

int main(){
	int N;
	//int x, y, vx, vy, r;
	bool no_aggs = true;
	cin >> N;
	vector<vector<double> > blobs;
	for(int i = 0; i < N; i++){
		vector<double> blob(5);
		//blobs.push_back(vector<int>(5));
		//x, y, vx, vy, r
		cin >> blob[0] >> blob[1] >> blob[2] >> blob[3] >> blob[4];
		blobs.push_back(blob);
	}	
			double t = 1e9 + 1;
	//cout << "got to the while loop" << endl;
	double total_t = 0;
	while(true){
		t = 1e9 + 1;
		pair<int, int> collid;
		for(int f = 0; f < blobs.size() - 1; f++){
			for(int s = f+1; s < blobs.size(); s++){
				//find the time of collision
				
				vector<double> first = blobs[f];  
				vector<double> second = blobs[s];
				double x0 = first[0];
				double y0 = first[1];
				double vx0 = first[2];
				double vy0 = first[3];
				double r0 = first[4];
				double x1 = second[0];
				double y1 = second[1];
				double vx1 = second[2];
				double vy1 = second[3];
				double r1 = second[4];
				double a = ((vx0 - vx1) * (vx0 - vx1)) + ((vy0 - vy1) * (vy0 - vy1));
				double b = 2*((x0*vx0) -(x1*vx0) -(x0*vx1) + (x1*vx1)
					         +(y0*vy0) -(y1*vy0) -(y0*vy1) + (y1*vy1));
				double c = ((x0 - x1) * (x0 - x1)) + ((y0 - y1) * (y0 - y1)) - ((r0 + r1)*(r0 + r1));
				double t1, t2;
				//cout << "a: " << a << " b: " << b << " c: " << c << endl;
				if(b*b - 4*a*c >= 0){
					t1 = (-b + sqrt(b*b - 4*a*c))/(2*a);
					t2 = (-b - sqrt(b*b - 4*a*c))/(2*a);
				} else {
					t1 = 1e9 + 2;
					t2 = 1e9 + 2;
				}
				if(t1 > 0){
					if(t1 < t){
						t = t1;
						collid = make_pair(f, s);
						no_aggs = false;
						//total_t += t;
					}
				}
				if(t2 > 0){
					if(t2 < t){
						//if(t1 > t){
						//	total_t -= t1;
						//}
						t = t2;
						collid = make_pair(f, s);
						no_aggs = false;
						
						//total_t += t;
					}
				}
			}
		}
		//cout << " got to an agg" << endl;
		//do the agglomeration
		if(t > 1e9){
			break;
		} else {
			total_t+=t;
			//cout << "AGG at " << t << " between " << collid.first << ", " << collid.second << endl;
			vector<double> newthing(5);
			int f = collid.first;
			int s = collid.second;
			vector<double> ff = blobs[f];
			vector<double> ss = blobs[s];
			double x0 = ff[0] + ff[2]*t;
			double y0 = ff[1] + ff[3]*t;
			double x1 = ss[0] + ss[2]*t;
			double y1 = ss[1] + ss[3]*t;
			double newarea = ff[4]*ff[4] + ss[4]*ss[4]; // whole thing times pi
			newthing[4] = sqrt(newarea);
			double fweight = (ff[4]*ff[4]) / (ff[4]*ff[4] + ss[4]*ss[4]);
			double sweight = (ss[4]*ss[4]) / (ff[4]*ff[4] + ss[4]*ss[4]);
			newthing[0] = fweight*x0 + sweight*x1;
			newthing[1] = fweight*y0 + sweight*y1;
			newthing[2] = fweight*ff[2] + sweight*ss[2];
			newthing[3] = fweight*ff[3] + sweight*ss[3];
			//cout << "hi" << endl;
			blobs.erase(blobs.begin() + max(f,s));
			blobs.erase(blobs.begin() + min(f,s));
			//cout << " hi again" << endl;
			
			//update everyone else's x and y to t
			//cout << blobs.size() << endl;
			for(int i = 0; i < (int)(blobs.size()); i++){
				//cout << i << endl;
				
				blobs[i][0] = blobs[i][0] + blobs[i][2]*t;
				blobs[i][1] = blobs[i][1] + blobs[i][3]*t;
			}

			//put newthing in
			//cout << "line 123" << endl;
			blobs.push_back(newthing);
			//cout << " after that " << endl;
		}
	}
	//cout << " got out of the while" << endl;
	//if(no_aggs){
		cout << fixed << (int)blobs.size() << " " << total_t << endl;
	//} else {
	//	cout << blobs.size() << " " << t << endl;
	//}
}