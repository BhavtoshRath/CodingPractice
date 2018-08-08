
class Solution:
    def rob(self, nums):
        last, now = 0, 0

        for i in nums:
            last, now = now, max(last + i, now)

        return now


s = Solution()
print(s.rob([2,7,9,3,1]))