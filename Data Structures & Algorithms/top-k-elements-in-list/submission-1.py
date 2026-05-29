class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frecuency = {}
        for n in nums:
            frecuency[n] = 1 + frecuency.get(n, 0)

        elements = []

        sorted_data = sorted(frecuency.items(), key=lambda item: item[1], reverse=True)
        i = 0
        while len(elements) < k:
            elements.append(sorted_data[i][0])
            i += 1
            
        return elements