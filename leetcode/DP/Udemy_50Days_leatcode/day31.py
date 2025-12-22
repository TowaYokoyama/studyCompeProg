"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(remaining, combo, start): #再帰のコア関数 reminig:まだつくらないといけない残りの合計,combo今まで選んできた数の組み合わせ, start 次に探すcandidatesのインデックス
            if remaining == 0:
                result.append(list(combo)) #合計がtargetに達したら結果に格納
            elif remaining < 0: #合計がtargetを超えたら
                return 
            
            elif remaining > 0:
                for i in range(start, len(candidates)):
                    combo.append(candidates[i])#結果を格納
                    backtrack(remaining - candidates[i],combo, i) #再帰呼び出し
                    combo.pop() #バックトラック 直前に追加した要素を取り消す 一歩戻る処理
                                                
                                                
        backtrack(target, [], 0)
        
        return result