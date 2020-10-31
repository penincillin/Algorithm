""" 
Longest Common Prefix, https://leetcode.com/problems/longest-common-prefix/
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return ""
        else:
            res = ""
            m = len(strs[0])
            for i in range(m):
                c = strs[0][i]
                not_succeed = False
                for str_ in strs[1:]:
                    if len(str_)>i and str_[i]==c:
                        pass
                    else:
                        not_succeed = True
                if not_succeed:
                    return res
                else:
                    res += c
            return res
        
        

def main():
    strs = ["flower","f","flight"]
    sol = Solution()
    res = sol.longestCommonPrefix(strs)
    print(res)

if __name__ == '__main__':
    main()
