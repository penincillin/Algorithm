#include <iostream>
using namespace std;

int mySqrt(int x){
    if (x==0) return 0;
    if (x<4)  return 1;
    int left=0, right=x;
    while(right-left>0){
        
        unsigned long long pivot = (left+right)/2;
        unsigned long long res = pivot*pivot;

        cout << left << " " << right << " " << pivot << endl;

        if(res>x) right=(left+right)/2;
        else left = (left+right)/2+1;

    }
    return right-1;
}

int main(){
    /*
    int is[5] = {1, 2, 4, 9, 10};
    for (int i=0; i<5; i++)
        cout << is[i] << " " << mySqrt(is[i]) << endl;
    */
    cout << mySqrt(2147395599) << endl;
    return 0;
}
