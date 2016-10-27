/* medium
 * this problem is a little hard for me, 
 * the main idea N = a0 * 2^0 + a1 * 2^1 + ... + an * 2^n
 * for example 24/5 = 20 + 4 = 2^2 * 5 + 2^0 *5, so the result is 2^2 + 2^0 = 4
 */


#include <iostream>
#include <stdlib.h>
using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        long long res = dividLong(dividend, divisor);
        if (res > INT_MAX || res < INT_MIN){
            return INT_MAX;
        }
        else{
            return res;
        }
    }
    long long dividLong(long long dividend, long long divisor){
        if(divisor == 0){
            return INT_MAX;
        }
        else{
            long long sign = dividend*divisor>=0 ? 1 : -1;
            dividend = abs(dividend);
            divisor = abs(divisor);
            long long res = 0;
            long long shift = 1;
            long long mid_div = divisor;
            while(dividend > mid_div){
                mid_div <<= 1;
                shift <<= 1;
            }
            if(dividend == mid_div){
                return shift*sign;
            }
            else{
                while(dividend >= divisor){
                    shift >>= 1;
                    if(dividend >= divisor*shift){
                        dividend -= divisor * shift;
                        res += shift;
                    }
                }

            }
            return sign * res;
        }
    }
};

int main(){
    int a = -4, b = 3;
    Solution ss;
    cout << ss.divide(a, b) << "\n";
    return 0;
}
