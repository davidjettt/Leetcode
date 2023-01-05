class Solution:
    def decodeString(self, s: str) -> str:
        '''
        input is a string
        integer to the left of square brackets indicates how many times need to repeat
        2[a] => aa
        2[abc] => abcabc

        if no

        '''

        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                
                stack.pop() #popping open bracket

                num_str = ''
                while stack and stack[-1].isdigit():  
                    num_str = stack.pop() + num_str
                stack.append(substr * int(num_str))

        return ''.join(stack)
