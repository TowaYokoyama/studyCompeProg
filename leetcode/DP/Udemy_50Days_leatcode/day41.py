"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}  # 対応表
        
        for char in s:
            if char in mapping.values():
                #閉じ括弧ならスタックに積む
                stack.append(char)
                
            elif char in mapping:
                #閉じ括弧なら対応を確認
                if not stack or stack [-1] != mapping[char]:
                    return False
                stack.pop()
        
            else:
                #括弧以外の文字が来た場合(今回は想定外)
                return False 
        
        #スタックが空ならすべて対応している
        return not stack