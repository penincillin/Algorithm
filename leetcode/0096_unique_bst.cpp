/* Unique Binary Search Trees, https://leetcode.com/problems/unique-binary-search-trees/
 */

#include <iostream>
#include <string>
#include <string.h>
#include <vector>
using namespace std;

class Solution {
public:
    int numTrees(int n) {
        int res[20];
        memset(res, 0, 20*4);
        res[0] = 1;
        res[1] = 1;
        for(int i=2; i<=n; i++){
            for(int j=0; j<i; j++){
                res[i] += res[j]*res[i-1-j];
            }
        }
        return res[n];
    }
};

int main(){
    Solution sol;
    int n = 4;
    int res = sol.numTrees(n);
    cout << res << "\n";
    return 0;
}
