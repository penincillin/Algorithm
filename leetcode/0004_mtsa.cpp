/* very good problem use divide and conquer and recursive algorithm */


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
private:
    double findKth(vector<int>& A, vector<int>& B, int k){
        if(A.size() > B.size())
            return findKth(B, A, k);
        if(A.size() == 0)
            return B[k-1];
        if(k==1)
            return min(A[0],B[0]);
        int pa=min(k/2, (int)A.size()), pb=k-pa;
        if(A[pa-1] < B[pb-1]){
            vector<int> newA(A.begin()+pa, A.end());
            return findKth(newA, B, k-pa);
        }
        else if (A[pa-1] > B[pb-1]){
            vector<int> newB(B.begin()+pb, B.end());
            return findKth(A, newB, k-pb);
        }
        else{
            return A[pa-1];
        }
    }
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m=nums1.size(), n=nums2.size();
        int total = m + n;
        if(total % 2 == 1)
            return findKth(nums1, nums2, total/2+1);
        else
            return (findKth(nums1, nums2, total/2) + 
                   findKth(nums1, nums2, total/2+1))/2;
    }
};

int main(){
    Solution ss;
    int A[4] = {2,3,6,10};
    vector<int> nums1(A, A+4);
    int B[4] = {1, 32, 243, 1111};
    vector<int> nums2(B, B+4);
    cout << ss.findMedianSortedArrays(nums1, nums2) << endl;
    return 0;
}
