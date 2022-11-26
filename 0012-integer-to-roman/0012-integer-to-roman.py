class Solution:
    def intToRoman(self, num: int) -> str:
        '''
            
        1 2 3
        
        I I I
        
        
        1 2 3 4 5
        
        V
        
        1 2 3 4 5 6 7 8 9 10 11 12 13 14
        
        I I I IV V VI VII VIII IX X XI XII XIII XIV
        
        XIV
        
        133 % 10 = 3
        CXXXIII
        
        thousands
        fivehundred
        onehundred
        fifty
        ten
        five
        one = IV
        
        XIV
        
        ones = 
        tens =  LXX
        hundreds = C
        thousands = ''
        
        "149"
         i
         
        turn input to a string
        iterate string
        compute roman numeral value at each position (tens, thousands, etc.)
        have conditionals for edges cases i.e 4s and 9s
        at the end concatenate all of the strings
          
        
        
        '''
        symbol_list = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400],['D', 500], ['CM', 900], ['M', 1000]]
        
        res = ''
        
        for sym, val in reversed(symbol_list):
            if num // val:
                count = num // val
                res += (count * sym)
            
            num = num % val
        return res
        
        
        
        
        
        