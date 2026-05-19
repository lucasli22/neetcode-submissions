class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            ans += str(len(string))
            ans += "#"
            ans += string
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        idx = 0 
        while idx < len(s):
            num = ""
            while idx < len(s) and s[idx] != "#":
                num += s[idx]
                idx += 1
            idx += 1
            num = int(num)
            ans.append(s[idx:idx+num])
            idx += num
        return ans
