import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        set_nums = set(nums)
        my_heap = []
        for n in set_nums:
            heapq.heappush(my_heap, n)

        print(my_heap)

        groups = []
        i = 0
        while len(my_heap) > 0:
            if not groups:
                groups.append([])

            smallest_num = heapq.heappop(my_heap)

            if len(groups[i]) == 0:
                groups[i].append(smallest_num)
            elif smallest_num - groups[i][-1] == 1:
                groups[i].append(smallest_num)
            else:
                groups.append([])
                i += 1
                groups[i].append(smallest_num)

        max_length = 0
        for g in groups:
            if max_length < len(g):
                max_length = len(g)

        return max_length
