/*
 * Spiral Matrix: https://leetcode.com/problems/spiral-matrix/
 */
#include <iostream>
#include <vector>
using namespace std;

template <typename T>
void print_vec(vector<T> vec){
    for(int i=0; i<vec.size(); i++){
        cout << vec[i] << " ";
    }
    cout << "\n";
}

template <typename T>
void print_vec_II(vector<vector<T>> vec){
    for(int i=0; i<vec.size(); i++){
        for(int j=0; j<vec[i].size(); j++){
            cout << vec[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "------------------\n";
}

int main(){
    vector<int> row1{1, 2, 3};
    vector<float> row2{1.1, 2.2, 3.3};
    vector<char> row3{'a', 'b', 'c'};

    print_vec<int>(row1);
    print_vec<float>(row2);
    print_vec<char>(row3);

    return 0;
}
