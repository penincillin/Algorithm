"""
Course Schedule II, https://leetcode.com/problems/course-schedule-ii/
topology sort
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        n = numCourses
        pre = prerequisites

        in_degrees = [0 for i in range(n)]
        neighbors = [list() for i in range(n)]

        for i0, i1 in pre:
            in_degrees[i0] += 1
            neighbors[i1].append(i0)

        queue = list()
        for i in range(n):
            if in_degrees[i] == 0:
                queue.append(i)

        res = list()
        while(len(queue)>0):
            cur = queue.pop(0)
            res.append(cur)
            for neigh in neighbors[cur]:
                in_degrees[neigh] -= 1
                if in_degrees[neigh] == 0:
                    queue.append(neigh)

        if len(res) == n:
            return res
        else:
            return []
        

def main():
    sol = Solution()
    n = 2
    pre = [
        [0, 1],
    ]
    res = sol.findOrder(n, pre)
    print(res)

  
if __name__ == '__main__':
    main()
