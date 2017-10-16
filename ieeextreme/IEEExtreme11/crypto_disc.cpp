#include <bits/stdc++.h>

using namespace std;

double dist[26][26];

double pi = 3.14159;
vector<char> letter(26);
vector<double> angle(26);

double d2r(double degree){
    return (pi * degree) / 180.0;
}

int main() {
    double r;
    cin >> r;
    vector<int> ltr(26);
    for(int i=0; i<26; i++){
        cin >> letter[i];
        ltr[letter[i] - 'A'] = i;
        cin >> angle[i];
        angle[i] = d2r(angle[i]);
    }
    
    for(int i=0;i<26;i++)
        for(int j=i+1;j<26;j++){
            
            double x1 = cos(angle[i]) * r;
            double y1 = sin(angle[i]) * r;
            
            double x2 = cos(angle[j]) * r;      
            double y2 = sin(angle[j]) * r;
            
            double dx = (x1-x2);
            double dy = (y1-y2);
            //dist[letter[i]-'A'][letter[j]-'A'] = sqrt(dx*dx+dy*dy);
            //dist[letter[j]-'A'][letter[i]-'A'] = sqrt(dx*dx+dy*dy);
            dist[i][j] = sqrt(dx*dx+dy*dy);
            dist[j][i] = sqrt(dx*dx+dy*dy);

            
        }
        
    double ans = r;
    string line;
    getline(cin, line);
    getline(cin, line);
    
    for(int i=0;i<line.size();i++){
        if(line[i] >= 'a' && line[i] <= 'z')
            line[i] += 'A' - 'a';
    }
    
    bool first = true;
    char last = 0;
    for(int i=0;i<line.size();i++){
        if(line[i] < 'A' || line[i] > 'Z')
            continue;
        if(first){
            first = false;
            last = line[i];
        }
        else{
            ans += dist[ltr[line[i]-'A']][ltr[last-'A']];
          //  cout << "! " << dist[line[i]-'A'][last-'A'] << endl;
            last = line[i];
        }
    }
    
    cout << ceil(ans) << endl;
}




