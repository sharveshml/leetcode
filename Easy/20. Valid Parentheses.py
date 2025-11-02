class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if stack and stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack and stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack and stack[-1] == '{' and i == '}':
                stack.pop()
            else:
                stack.append(i)
        
        if stack:
            return False 
        else:
            return True