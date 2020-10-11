#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

void print_vec(vector<int> vec){
    for (auto it = vec.begin(); it!=vec.end(); it++){
        cout << *it << " ";
    }
    cout << "\n";
}

int main(){
    int A[] = {1,2,3};

    vector<int> v1(A, A+3);
    print_vec(v1);

    vector<int> v2{1,2,3};
    print_vec(v2);

    vector<int> v3{0,0,0};
    print_vec(v3);

    return 0;
}
