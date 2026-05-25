class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pre = 0
        suf = len(numbers) - 1
        while suf > pre:
            total = numbers[pre] + numbers[suf] 
            if total == target:
                return [pre+1,suf+1]
            elif total > target:
                suf -= 1
            elif total < target:
                pre += 1
            