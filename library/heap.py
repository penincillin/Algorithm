import heapq


def main():
    nums = [1,2,3,4,0]
    heapq.heapify(nums)

    # top
    top_val = nums[0]
    print(top_val)

    # heap push
    heapq.heappush(nums, -1)
    print(nums[0])

    # heap pop
    top_val = heapq.heappop(nums)
    print(top_val)

    # n-smallest value
    n_small = heapq.nsmallest(3, nums)
    print(n_small)



if __name__ == '__main__':
    main()
