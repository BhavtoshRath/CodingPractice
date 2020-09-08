# Maximize sth...
# for some array qs sorting first could be a start....

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sum = 0
        for i in range(0, len(nums), 2):
            sum += min(nums[i], nums[i+1])

        return sum


s = Solution()
print(s.arrayPairSum([1,4,3,2]))