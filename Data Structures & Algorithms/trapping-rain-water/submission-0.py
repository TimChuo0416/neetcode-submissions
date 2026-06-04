class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0]*len(height)
        suf = [0]*len(height)
        length = len(height) - 1
        total = 0
        for i, h in enumerate(height):
            if i > 0:
                pre[i] = max(pre[i-1],height[i-1])
                suf[length - i] = max(suf[length - i + 1],height[length - i + 1])
        print(pre,suf)
        for i, h in enumerate(height):
            total += max( min(pre[i],suf[i]) - h ,0)
            
        return total


        