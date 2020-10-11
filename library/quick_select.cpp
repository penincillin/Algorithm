#include <iostream>
#include <assert.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
using namespace std;

void print_A(int *A, int head, int tail){
    for(int i=head; i<tail+1; i++){
        cout << A[i] << " ";
    }
    cout << "\n";
}

int partition(int* A, int head, int tail){
    int pivot = A[tail]; // chose tail as pivot
    //int head0=head, tail0=tail;
    while (head < tail){
        while(head < tail & A[head] <= pivot){
            head += 1;
        }
        if (head < tail){
            A[tail] = A[head];
            A[head] = pivot;
            tail -= 1;
        }
        while(head < tail & A[tail] >= pivot){
            tail -= 1;
        }
        if (head < tail){
            A[head] = A[tail];
            A[tail] = pivot;
            head += 1;
        }
    }
    return head;
}

int quick_select(int* A, int k, int head, int tail){
    if (head >= tail){
        return A[head];
    }

    int p = partition(A, head, tail); // this partition() always returns absolute index of whole A

    if (p == k){
        return A[p];
    }
    else if (p < k) {
        return quick_select(A, k, p+1, tail);
    }
    else{
        return quick_select(A, k, head, p-1);
    }

}

// {{{
void check_batch(){
    for (int n=0; n<100000; n++){
        int num_data = 10;
        srand(time(NULL));
        int *A = new int[num_data];
        int *B = new int[num_data];
        int *C = new int[num_data];
        for (int i=0; i<num_data; i++){
            A[i] = rand() % 10;
            B[i] = A[i];
            C[i] = A[i];
        }

        int k = rand() % num_data;

        int res0 = quick_select(A, k, 0, num_data-1);

        sort(B, B+num_data);
        int res1 = B[k];

        assert (res0 == res1);

        delete [] A;
        delete [] B;
    }
}


void check_one(){
    int A[] = {3, 6, 0, 7, 0, 4, 1, 4, 2, 8};
    int num_data = sizeof(A) / sizeof(A[0]);
    int k = 7;

    int res = quick_select(A, k, 0, num_data-1);
    cout << res << "\n";

}

int main(){
    check_batch();
    return 0;
}
