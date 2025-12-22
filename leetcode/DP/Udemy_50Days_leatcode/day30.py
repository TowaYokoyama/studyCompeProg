"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
#上下左右が道として通れるかってこと
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # すべての文字を見つけたら True
            if i == len(word):
                return True
            # 範囲外 or 不一致 or 再訪問なら False
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != word[i]):
                return False

            # 現在の文字を一時的に使用済みにする
            temp = board[r][c]
            board[r][c] = "#"  # マーク（訪問済み）

            # 十字方向（上下左右）に探索を伸ばす
            res = (dfs(r+1, c, i+1) or  # 下
                   dfs(r-1, c, i+1) or  # 上
                   dfs(r, c+1, i+1) or  # 右
                   dfs(r, c-1, i+1))    # 左

            # 戻す（バックトラック）
            board[r][c] = temp
            return res

        # 全セルをスタート点として試す
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
