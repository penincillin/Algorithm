#include <iostream>
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
    while (head < tail){
        while(head < tail & A[head] <= pivot){
            head += 1;
        }
        if (head < tail){
            A[tail] = A[head];
            tail -= 1;
        }
        while(head < tail & A[tail] >= pivot){
            tail -= 1;
        }
        if (head < tail){
            A[head] = A[tail];
            head += 1;
        }
    }
    A[head] = pivot;
    return head;
}

void quick_sort(int* A, int head, int tail){
    if (head < tail){
        int p = partition(A, head, tail);
        quick_sort(A, head, p-1);
        quick_sort(A, p+1, tail);
    }
}

int main(){
    for (int n=0; n<1000; n++){
        int num_data = 10000;
        srand(time(NULL));
        int *A = new int[num_data];
        int *B = new int[num_data];
        for (int i=0; i<num_data; i++){
            A[i] = rand() % 100 + 1;
            B[i] = A[i];
        }

        quick_sort(A, 0, num_data-1);
        sort(B, B+num_data);

        for (int i=0; i<num_data; i++){
            assert (A[i] == B[i]);
        }

        delete [] A;
        delete [] B;
    }
    return 0;
}
