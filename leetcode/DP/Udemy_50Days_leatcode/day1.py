class Solution(object):
    def maxArea(self, height):
        # 左端と右端のポインタを用意する
        left, right = 0, len(height) - 1
        # 最大面積を記録する変数
        max_area = 0
        
        # 左と右のポインタが交差するまで繰り返す
        while left < right:
            # 現在の容器の面積を計算
            # 幅 = (right - left)
            # 高さ = 2本のうち小さい方（min）
            area = (right - left) * min(height[left], height[right])
            # 最大面積を更新（もし現在の area が大きければ差し替え）
            max_area = max(max_area, area)
            
            # 小さい方の線を動かす（大きい方を動かしても面積は増えないため）
            if height[left] < height[right]:
                left += 1  # 左を右に1つ寄せる
            else:
                right -= 1  # 右を左に1つ寄せる
        
        # 最終的に求めた最大面積を返す
        return max_area
