class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_map = {}
        res = 0 
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            frequency_map[char] = 1 + frequency_map.get(char, 0)
    
            most_frequent_char = max(frequency_map, key=frequency_map.get)
            
            if right - left + 1 - frequency_map[most_frequent_char] > k:
                frequency_map[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            
            # if window_length - frequency_map[most_frequent_char] <= k:
            #     res = right - left + 1
            # else:
            #     frequency_map[s[left]] -= 1
            #     left += 1
                # most_frequent_char = max(frequency_map, key=frequency_map.get)
                # if right - left + 1 - frequency_map[most_frequent_char] <= k:
                #     res = right - left + 1
        return res
            
            
            
        
        