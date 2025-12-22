"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
「s の中で、t に必要な文字をすべて含むような、最短の区間（部分文字列）」
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter 
        
        #tの各文字の必要性をカウント
        need = Counter(t)
        missing = len(t) #まだ満たしていない文字の数
        
        left = start = end = 0 #start,endは結果のインデックス
        for right,char in enumerate(s,1):
            if need[char]>0:
                missing -=1
            need[char]-=1
            
            #すべての文字がそろったら(missing=0)
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
            
            #現在のウィンドを結果候補にする
                if end == 0 or right -left < end -start:
                    start,end = left,right 
            
            #もう一度missing状態にして次の候補をさがす
                need[s[left]] += 1
                missing +=1 
                left+=1
        return s[start:end]