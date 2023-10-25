
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        valToIndex = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in valToIndex:
                return [valToIndex[need], i]
            valToIndex[nums[i]] = i
        return []
        
# leetcode submit region end(Prohibit modification and deletion)
