class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, current_combination):
            # Base case: if the current combination reaches the length of digits
            if index == len(digits):
                result.append("".join(current_combination))
                return

            # Get letters corresponding to the current digit
            possible_letters = digit_to_letters[digits[index]]

            # Explore each letter choice recursively
            for letter in possible_letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()  # Backtrack step

        backtrack(0, [])
        return result