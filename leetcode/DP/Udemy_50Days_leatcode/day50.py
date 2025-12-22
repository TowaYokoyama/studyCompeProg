"""
Given a string s, return the longest palindromic substring in s.(回文)
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb" 
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            # 左右に広げて、回文が続く限り広げる
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # whileを抜けたときは1つ外に出てるので、[l+1:r] が回文
            return s[l+1:r]
        res = ""
        for i in range(len(s)):
            # 奇数長（aba 型）
            odd = expand(i, i)
            # 偶数長（abba 型）
            even = expand(i, i+1)
            # どちらが長いか比べる
            res = max(res, odd, even, key=len)
        return res
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s 
        # dp[i][j]：s[i:j+1] が回文なら True
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1  # 最長の開始位置と長さ
        #1文字なら回文とする
        for i in range(n):
            dp[i][i] = True 
        
        #2文字の場合
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] =True
                start,max_len = i,2

        #長さ3文字以上
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length -1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start,max_len = i,length
            
        return s[start:start + max_len]