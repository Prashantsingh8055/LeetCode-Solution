class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # Base condition: a valid combination of length 2*n is formed
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Rule 1: We can add an '(' if we haven't used all n open parentheses
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Rule 2: We can add a ')' only if it doesn't exceed open parentheses
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result