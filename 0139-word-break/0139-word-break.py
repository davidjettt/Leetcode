class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''

           go though input string
           adding char into prefix string
            (check if input string == prefix)
                if true, then we have reach end of input string
                return true if this final prefix is in wordDict
           check if prefix is in wordDict
            if true, do recursive call on suffix

          if we iterate through entire input string without finding prefix in wordDict then return false

        aaaaaaa
        pre = aaa
        suf = aaaa

        aaaa
        pre = aaaa
        suf = a

        a
        pre = a
        returns false
        {suffix: boolean indicating if it is in wordDict}

        '''
        wordDict2 = set(wordDict)
        memo = {}
        def dfs(s):
            prefix = ''
            if s in memo:
                return memo[s]
            for i in range(len(s)):
                prefix += s[i]
                if prefix in wordDict2:
                    memo[prefix] = True
                    if prefix == s:
                        return True
                    else:
                        res = dfs(s[i+1:])
                        if res == True:
                            return True
            memo[prefix] = False
            return False
        return dfs(s)
        