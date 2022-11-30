class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        A B A B  k=2
        
        
        res = 1
        
        {
          'A': 0,
          'B': 1,
        }
        
        1 - 1 = 0
        
        
        A A B A B B A   k=1
                l     r
                
        A B C A B C    k=2
            l     r
            
            
        A B A B  k=0
         lr
        
        iterate though string
            add char to hashmap
            
            subtract most frequent char count with window length
            
            use that number to compare with k
            if that number is <= k, that means we can make a longer valid substring
                compare result with window length and get the bigger
            if that number is > k, then need to move left pointer cause current window not valid
                use while loop to move left pointer until current window is back to being valid by performing the same check
                
                
        return result
        
        Time O(n) where n is the length of the input string
        Space O(1)
        '''
        
        res = 0
        chars = {}
        l = 0
        
        for r in range(len(s)):
            chars[s[r]] = 1 + chars.get(s[r], 0)
            
            while (r - l + 1) - max(chars.values()) > k:
                chars[s[l]] -= 1
                l += 1
            
            # if (r - l + 1) - max(chars.values()) <= k:
            res = max(res, r - l + 1)
                    
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Time O(26n)
        # Space O(1)
        frequency_map = {}
        res = 0 
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            frequency_map[char] = 1 + frequency_map.get(char, 0)
    
            most_frequent_char = max(frequency_map, key=frequency_map.get)  # This is what causes it to be O(26n) Time
            
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
            
            
            
        
        