"""
Course Schedule, https://leetcode.com/problems/course-schedule/
Topology sort,
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
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

        while(len(queue)>0):
            cur = queue.pop(0)
            n -= 1
            for neigh in neighbors[cur]:
                in_degrees[neigh] -= 1
                if in_degrees[neigh] == 0:
                    queue.append(neigh)
        return n == 0
        

def main():
    sol = Solution()
    n = 2
    pre = [
        [0, 1],
        [1, 0],
    ]
    res = sol.canFinish(n, pre)
    print(res)

  
if __name__ == '__main__':
    main()
