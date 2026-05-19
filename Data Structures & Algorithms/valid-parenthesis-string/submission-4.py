class Solution:
    def checkValidString(self, s: str) -> bool:
        aStack = []
        lStack = []
        for i, ch in enumerate(s):
            if ch == "(":
                lStack.append(i)
            elif ch == "*":
                aStack.append(i)
            else:
                if lStack:
                    lStack.pop()
                else:
                    if aStack:
                        aStack.pop()
                    else:
                        return False
        
        while lStack:
            if not aStack:
                return False
            index = lStack.pop()
            found = False
            while aStack:
                if aStack.pop() > index:
                    found = True
                    break

            if not found:
                return False
            
        return True

        
        