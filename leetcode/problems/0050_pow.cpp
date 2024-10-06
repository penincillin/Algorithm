/*
 * Pow: https://leetcode.com/problems/powx-n/submissions/
 * Use classical quick pow algorith to solve it. Reference:https://oi-wiki.org/math/quick-pow/
 */
#include <iostream>
#include <math.h>

using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0){
            return 1.0;
        }
        double res = 1.0;
        bool minus = false;
        long long n1 = n;
        if (n1<0){
            n1 *= -1;
            minus = true;
        }

        double m = x;
        while(n1>0){
            if (n1 % 2 != 0){
                res *= m;
            }
            n1 = n1>>1;
            m *= m;
        }

        if (minus){
            return 1.0/res;
        }
        else{
            return res;
        }

    }
};

int main(){
    Solution sol;

    double x = 2.1;
    int n = 3;

    double res = sol.myPow(x, n);
    cout << res << "\n";
}
