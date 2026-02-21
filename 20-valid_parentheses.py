class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', ')':'(', '{':'}', '}':'{', '[':']', ']':'['}
        chars = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                chars.append(c)
            elif c == ')' or c == ']' or c== '}':
                if chars:
                    if chars[-1] == pairs[c]:
                        chars.pop()
                        continue 
                chars.append(c)
        return len(chars) == 0
