class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(n*m)
        # set1 = set(nums1)
        # greaterEle = {}

        # for i in range(len(nums2)):
        #     curN = nums2[i]

        #     if curN in set1:
        #         greaterEle[curN] = -1
        #         for j in range(i + 1, len(nums2)):
        #             if nums2[j] > curN:
        #                 greaterEle[curN] = nums2[j]
        #                 break

        # for i in range(len(nums1)):
        #     nums1[i] = greaterEle[nums1[i]]

        # return nums1

        # O (n + m)
        nums1Idx = { n:i for i, n in enumerate(nums1) }
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]

            # while stack exists and current is greater than the top of the stack
            while stack and cur > stack[-1]:
                val = stack.pop() # take top val
                idx = nums1Idx[val]
                res[idx] = cur

            if cur in nums1Idx:
                stack.append(cur)
        
        return res