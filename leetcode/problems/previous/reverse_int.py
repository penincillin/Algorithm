class Solution(object):
    def reverse(self, x):
        s_num = str(x)
        res = 0
        if s_num[0]=='-':
            s_num = s_num[1:]
            res = int('-'+s_num[::-1])
        else:
            res = int(s_num[::-1])
        if res<-2147483648 or res>2147483647: return 0
        else: return res
        
if __name__ == '__main__':
    ss = Solution()
    print ss.reverse(-123)
    print ss.reverse(123)

        
