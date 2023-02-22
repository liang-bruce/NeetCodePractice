class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l, r = 0, 0

        while r < len(nums):
            # remove & update window's left boundary when size exceeds limit 
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
            r += 1

        return False