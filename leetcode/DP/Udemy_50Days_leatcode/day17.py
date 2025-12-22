"""
 Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}  # 普通の辞書

        for s in strs:
            # 各文字の出現回数を数える
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1  #ord() は「文字を数字（Unicodeの番号）」に変える関数。
            #インデックスがに対して1を足すからこうなる　count = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            # 辞書のキーに使えるようにタプル化
            key = tuple(count)

            # 🔽 defaultdictがないから、自分でif文で初期化する
            if key not in seen:
                seen[key] = []
            seen[key].append(s)

        # value部分をリストで返す
        return list(seen.values())
"""
        {
  (1,0,0,0,1,0,0,0,...,1,...): ["eat", "tea", "ate"],
  (1,0,0,0,0,0,0,0,...,1,1,...): ["tan", "nat"],
  (1,0,0,0,0,0,1,0,...,1,...): ["bat"]
}

"""

