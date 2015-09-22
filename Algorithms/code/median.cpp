/* This code implemention algorithm in page 54 */
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <algorithm>
#include <vector>

using namespace std;

int find_k_smallest_silly(int *A, int N, int k){
    /*this algorithm's complexity is O(nlogn) */
    assert(k <= N);
    sort(A, A+N);
    return A[k-1];
}

int find_k_smallest_smart(int *A, int N, int k){
    /* this algorithm's complexity is O(n) */

    assert(k <= N);
    /* split N into 3 parts: less than pivot, equal to pivot,bigger than pivot */
    int pivot = A[N/2];
    int tmp = 0;
    for(int i=0; i<N; i++){
        if(A[i]<pivot){
            swap(A[tmp], A[i]);
            tmp++;
        }
    }
    int lenL = tmp;
    for(int i=tmp; i<N; i++){
        if(A[i]==pivot){
            swap(A[tmp], A[i]);
            tmp++;
        }
    }

    /* find result in three different sub arrays */
    if(k<=lenL) return find_k_smallest_smart(A, lenL, k);
    if(k>tmp)   return find_k_smallest_smart(A+tmp, N-tmp, k-tmp);
    return pivot;

}

int main(){
    srand(time(NULL));
    for(int iter=0; iter<10; iter++){
        int N = rand()%1000;
        int k = rand()%N;

        int A[N];
        for(int i=0; i<N; i++) 
            A[i] = rand()%10000;

        int res2 = find_k_smallest_smart(A, N, k);
        int res1 = find_k_smallest_silly(A, N, k);
        cout << res1 << " vs " << res2 << endl;
    }
    return 0;
}
