#include <iostream>
#include <map>

using namespace std;

int f(int i){
    if(i < 3) return 0;
    if(i >= 3 && i < 6) return 3;
    if(i >= 6 && i < 9) return 6;
    return 0;
}

int g(int i){
    if(i < 3) return 3;
    if(i >= 3 && i < 6) return 6;
    if(i >= 6 && i < 9) return 9;
    return 0;
}

int main(){

    int a[9][9];
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            cin >> a[i][j];
        }
    }

    map <int, int> row;
    map <int, int> column;
    map <int, int> cube;

    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            if(a[i][j] == 0){
                for(int x = 0; x < 9; x++){
                    row[a[i][x] + 1]++;
                    column[a[x][j] + 1]++;
                }
                for(int c = f(i); c < g(i); c++){
                        for(int b = f(j); b < g(j); b++){
                            cube[a[c][b] + 1]++;
                        }
                    }
                for(int k = 1; k <= 9; k++){
                    if(!row[k] && !column[k] && !cube[k]){
                        a[i][j] = k;
                        break;
                    }
                }        
            }
        }
        row.clear();
        column.clear();
        cube.clear();
    }

    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            cout << a[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}