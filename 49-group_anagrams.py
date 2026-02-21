class Solution:
    def groupAnagrams(self, strs: list[str]):
        anagrams = {} 
        for s in strs:
            letters = frozenset(list(s))
            if letters not in anagrams:
                anagrams[letters] = [s]
            else:
                anagrams[letters].append(s)
        result = [value for value in anagrams.values()]
        return result


sol = Solution()
print(sol.groupAnagrams(["ddddddddddg","dgggggggggg"]))