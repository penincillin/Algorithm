import heapq


def main():
    heap = list()
    heapq.heapify(heap)
    heapq.heappush(heap, 'a')
    heapq.heappush(heap, 'b')
    heapq.heappush(heap, 'c')

    print(heapq.heappop(heap), len(heap))
    print(heapq.heappop(heap), len(heap))
    print(heapq.heappop(heap), len(heap))


if __name__ == '__main__':
    main()
