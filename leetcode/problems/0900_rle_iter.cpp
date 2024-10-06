/*
RLE Iterator, https://leetcode.com/problems/rle-iterator/
The problem is hard. The only thing to pay attention is that the idea of directly extending the array is not time efficient.
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <string>
#include <map>
#include <unordered_map>
#include <set>
#include <array>
using namespace std;

template<typename T>
void print_array(T A[], int size){
    for(int i=0; i<size; i++){
        cout << A[i] << " ";
    }
    cout << "\n";
}

template <typename T>
void print_vec(vector<T> vec){
    for(auto v:vec){
        cout << v << " ";
    }
    cout << "\n";
}

class RLEIterator {
private:
    vector<int> array;
    vector<int>* encoding;
    bool use_decode;
    bool use_inplace;
    int a_idx;
    int e_idx;

    void solve_decode(){
        use_decode = true; use_inplace = false;
        a_idx = 0;

        int n = (*encoding).size();
        for(int i=0; i<n; i+=2){
            int repeat=(*encoding)[i];
            int num=(*encoding)[i+1];
            for(int j=0; j<repeat; j++){
                array.push_back(num);
            }
        }
        // print_vec(array);
    }

    int next_decode(int n){
        a_idx += n;
        if (a_idx <= array.size()){
            return array[a_idx-1];
        }
        else{
            return -1;
        }
    }

    void solve_inplace(){
        use_decode = false; use_inplace = true;
        e_idx = 0;
    }

    int next_inplace(int n){
        if (e_idx > (*encoding).size()-2){
            return -1;
        }
        else{
            int repeat=(*encoding)[e_idx];
            int num=(*encoding)[e_idx+1];
            while(n > repeat && e_idx <= (*encoding).size()-2){
                n -= repeat;
                e_idx += 2;
                repeat=(*encoding)[e_idx];
                num=(*encoding)[e_idx+1];
            }
            if(e_idx <= (*encoding).size()-2 && n <= repeat){
                (*encoding)[e_idx] -= n;
                return (*encoding)[e_idx+1];
            }
            else if(e_idx <= (*encoding).size()-2 && n > repeat){
                (*encoding)[e_idx] -= n;
                return -1;
            }
            else{
                return -1;
            }
        }
    }


public:
    RLEIterator(vector<int>& encoding) {
        this->encoding = &encoding;
        // solve_decode();    
        solve_inplace();
    }
    
    int next(int n) {
        if (use_decode){
            return next_decode(n);
        }
        else{
            return next_inplace(n);
        }
        
    }
};

int main(){
    vector<int> encoding, nexts;
    encoding = {3, 8, 0, 9, 2, 5};
    nexts = {2, 1, 1, 2};

    RLEIterator rle_iter(encoding);

    for (auto n : nexts){
        int res = rle_iter.next(n);
        cout << n << " " << res << "\n";
    }
    return 0;
}
