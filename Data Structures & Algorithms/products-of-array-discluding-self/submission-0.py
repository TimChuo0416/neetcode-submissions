class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1] * l
        suf = [1] * l
        res = [0] * l
        total = 1
        for i in range(l - 1):
            pre[i + 1] = pre[i] * nums[i]
            suf[l - i - 2] = suf[l - i -1] * nums[l - i - 1]
        for i in range(l):
            res[i] = pre[i] * suf[i]
        return res
            