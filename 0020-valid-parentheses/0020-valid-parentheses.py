class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in mapping:
                # If stack is not empty, pop the top element; otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped bracket matches the mapping
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched correctly
        return not stack