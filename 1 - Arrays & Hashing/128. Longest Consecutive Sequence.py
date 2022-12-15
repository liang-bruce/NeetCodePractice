class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # visualise it in a 数轴
        # use a set to achieve fast lookup
        # starting element has no leftNeighbour, ending element has no rightNeighbour
        
        # convert to a set
        numsSet = set(nums)

        # loop through the set to 
        #    if it is the starting element
        #       find the length of the sequence
        #       compare the length and the max length
        #    else
        #       move on  

        maxLength = 0
        for num in numsSet:
            if (num - 1) not in numsSet:
                currLength = 1
                currNum = num
                while (currNum + 1) in numsSet:
                    currNum += 1
                    currLength += 1
                maxLength = max(maxLength, currLength)
        return maxLength