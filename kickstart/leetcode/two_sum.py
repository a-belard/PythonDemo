class Solution:
    def twoSum(self, nums, target: int):
        n = int(len(nums) / 2)
        if len(nums) % 2 != 0:
            diff = target - nums[n]
            try:
                k = nums.index(diff)
                return [n, k]
            except ValueError:
                pass
        for i in range(n):
            diff = target - nums[i]
            diff2 = target - nums[0 - i - 1]
            try:
                k = nums.index(diff)
                if k != i and nums[k] == diff:
                    return [i, k]
            except ValueError:
                pass
            try:
                k2 = nums.index(diff2)
                if k2 != len(nums)-1-i and nums[k2] == diff2:
                    return [k2, len(nums) - i - 1]
            except ValueError:
                pass

twosum = Solution()
print(twosum.twoSum([1,6142,8192,10239],18431))