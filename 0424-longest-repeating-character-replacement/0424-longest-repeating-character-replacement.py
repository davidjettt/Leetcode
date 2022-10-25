class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        frequency_map = {}
        
        # for c in s:
        #     if c not in frequency_map:
        #         frequency_map[c] = 1
        #     else:
        #         frequency_map[c] += 1
        
        # A A B A B B A
        #   l     r
        
        #.  A  B  A  A
        #.        l  r
        
        res = 0 
        # left, right = 0, 0
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            if char in frequency_map:
                frequency_map[char] += 1
            else:
                frequency_map[char] = 1
    
            most_frequent_char = max(frequency_map, key=frequency_map.get)
            window_length = right - left + 1
            
            if window_length - frequency_map[most_frequent_char] <= k:
                res = right - left + 1
            else:
                frequency_map[s[left]] -= 1
                left += 1
                most_frequent_char = max(frequency_map, key=frequency_map.get)
                if right - left + 1 - frequency_map[most_frequent_char] <= k:
                    res = right - left + 1
        return res
            
            
            
        
        