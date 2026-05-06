class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr_dict = {}
        for e in nums:
            if e in arr_dict:
                return True
            arr_dict[e] = 1
        return False

            