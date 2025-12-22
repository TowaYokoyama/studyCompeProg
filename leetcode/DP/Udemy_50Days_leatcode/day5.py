class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # 重複がある場合、左ポインタを進める
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            # 右の文字をセットに追加
            seen.add(s[right])

            # 最大長を更新
            max_len = max(max_len, right - left + 1)

        return max_len
