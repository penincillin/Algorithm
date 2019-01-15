#include <iostream>
using namespace std;

void print_array(int *A, int lo, int hi){
    for(int i=lo; i<=hi; i++){
        cout << A[i] << " ";
    }
    cout << "\n";
}

int partition(int *A, int lo, int hi);

void quick_sort(int *A, int lo, int hi){
    /* index of A ranges in [lo, hi] */

    int p = partition(A, lo, hi);
    if (p>=0) {
        quick_sort(A, lo, p-1);
        quick_sort(A, p+1, hi);
    };
}

int partition(int *A, int lo, int hi){

    if (lo < hi){
        int pivot = A[lo];
        while( lo < hi){
            while ( hi>lo && A[hi]>=pivot ){
                hi--;
            }
            if (lo < hi){
                A[lo] = A[hi];
                lo++;
            }

            while( hi>lo && A[lo]<=pivot){
                lo++;
            }
            if (lo < hi){
                A[hi] = A[lo];
            }
        }

        A[lo] = pivot;
        return lo;
    }
    else{
        return -1;
    }
}

int main(){

    int N = 0;
    cin >> N;
    int A[N];
    for(int i=0; i<N; i++){
        cin >> A[i];
    }

    quick_sort(A, 0, N-1);

    print_array(A, 0, N-1);
    return 0;
}
