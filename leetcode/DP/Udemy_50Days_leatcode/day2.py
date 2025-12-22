#　与えられた配列が山の形かどうかをtrue/falseで返す関数を実装するっていう問題のこと！

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 1 
        # 上り坂
        while i < n and arr[i] > arr[i-1]:
            i += 1

        # 頂点が最初 or 最後ならダメ
        if i == 1 or i == n:
            return False

        # 下り坂
        while i < n and arr[i] < arr[i-1]:
            i += 1

        # 配列の最後まで到達できたら山
        return i == n
