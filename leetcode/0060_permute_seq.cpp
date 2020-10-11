/* Permutation Sequence, https://leetcode.com/problems/permutation-sequence/
 * The solution is straightforward, just write down n=3 or n=4 to find the law
 */

#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string getPermutation(int n, int k) {
        int fact[n+1];
        fact[0] = 1;
        for(int i=1; i<=n; i++){
            fact[i] = fact[i-1] * i;
        }

        bool used[n+1];
        memset(used, 0, n+1);

        int depth = 0;
        string res = "";
        while(depth < n){
            int cur = (k-1) / fact[n-depth-1];
            int count = 0;
            string mid_res = " ";
            for(int i=0; i<n; i++){
                if (! used[i]){
                    if (count == cur){
                        mid_res[0] = '1'+i;
                        used[i] = true;
                        break;
                    }
                    else{
                        count ++;
                    }
                }
            }
            res += mid_res;
            k -= fact[n-depth-1]*cur;
            depth ++;
        }
        return res;
    }
};

int main(){
    int n = 3, k = 3;

    Solution sol;
    string res = sol.getPermutation(n, k);
    cout << res << "\n";
    return 0;
}
