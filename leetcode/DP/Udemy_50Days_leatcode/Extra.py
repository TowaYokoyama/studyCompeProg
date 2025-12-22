# https://leetcode.com/problems/the-skyline-problem/submissions/1796861662
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        入力: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
出力: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
説明:
図 A は入力の建物を示しています。
図Bは、これらの建物によって形成されるスカイラインを示しています。図Bの赤い点は、出力リストのキーポイントを表しています。
例2:

入力: buildings = [[0,2,3],[2,5,3]]
出力: [[0,3],[5,0]]
 

制約:

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings非降順でソートされます。
lefti
        """
        events = []
        #イベントの転換点を作る 建物の左端と右橋をイベントとする
        for left,right,height in buildings:
            events.append((left,-height))
            events.append((right,-height))
            
        #ソート
        events.sort(key=lambda x: (x[0], x[1]))
        
        #結果を保存するためのリストとheapq
        result = [[0,0]]
        heapq = [0]#現在の高さ
        active={0:1} #各高さの出現回数
        for x,h in events:
            if h<0:
                #startイベント⇒高さを追加
                heapq.heappush(heap,h)
                active[-h] = active.get(-h,0)+1
            else:
                # endイベント → 高さを削除（カウント減少）
                active[h] -= 1
                if active[h] == 0:
                    del active[h]

            # 現在の最大高さを求める
            while -heap[0] not in active:
                heapq.heappop(heap)

            curr_height = -heap[0]

            # 高さが変わった場合のみ追加
            if result[-1][1] != curr_height:
                result.append([x, curr_height])

        return result[1:]  # 最初のダミーを除去
    
    #heapq二分木で保存する感じ