class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
            
        result = []
        
        # Run sliding window for each possible word alignment offset
        for i in range(word_len):
            left = i
            current_count = {}
            count = 0
            
            # Step through the string in increments of word_len
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j+word_len]
                
                if word in word_count:
                    current_count[word] = current_count.get(word, 0) + 1
                    count += 1
                    
                    # If a word occurs more times than permitted, shrink the window from the left
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len
                        
                    # If the valid word count matches the target, record the starting index
                    if count == num_words:
                        result.append(left)
                else:
                    # Reset the window if an invalid word is encountered
                    current_count.clear()
                    count = 0
                    left = j + word_len
                    
        return result