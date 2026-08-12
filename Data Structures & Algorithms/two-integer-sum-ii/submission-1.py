class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, n in enumerate(numbers):
            num_dict[n] = i
        
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in num_dict and num_dict[diff] != i:
                return [i + 1, num_dict[diff] + 1]
        return []
