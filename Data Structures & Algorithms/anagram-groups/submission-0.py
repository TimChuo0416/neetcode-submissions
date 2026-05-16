class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # map (a-z count) -> str
        for s in strs:
            count = [0] * 26 # a-z count
            for c in s:
                count[ord(c)- ord('a')] += 1
            result[tuple(count)].append(s)
        
        return list(result.values())