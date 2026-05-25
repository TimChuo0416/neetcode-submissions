class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pre = 0
        suf = len(numbers) - 1
        while suf > pre:
            if numbers[pre] + numbers[suf] == target:
                return [pre+1,suf+1]
            elif numbers[pre] + numbers[suf] > target:
                suf -= 1
            elif numbers[pre] + numbers[suf] < target:
                pre += 1
            