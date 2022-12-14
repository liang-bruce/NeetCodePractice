class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create 1 hashmap to store element: frequency
        # create a list of list to store frequency: element pair 
        # (index being the frequency, inner list contains all elements with corresponding frequency)
        # knowing the max frequency will be len(nums)
        count = {}
        freqElementMap = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for n, f in count.items():
            freqElementMap[f].append(n)
        
        result = []
        for i in range(len(freqElementMap)-1, 0, -1):
            for num in freqElementMap[i]:
                result.append(num)
                if len(result) == k:
                    return result
