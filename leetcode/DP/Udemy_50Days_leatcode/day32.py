"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
回文 partition
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
部分文字列とは元の文字列の中で連続した部分だけを取り出したもの
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def dfs(start,path):
            if start >= len(s):
                result.append(list(path))
                return 
            
            for end in range(start, len(s)):
                substring = s[start:end +1]
                if substring == substring[::-1]: #回文チェック
                    path.append(substring)#ここが必須
                    dfs(end +1,path) #再帰
                    path.pop() #戻す
        
        dfs(0,[])
        return result
            