class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord("a")] += 1
            key = tuple(freq)
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
        ans = []
        for val in anagrams.values():
            ans.append(val)
        return ans