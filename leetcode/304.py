"""
leetcode.304 の Docstring
2D行列matrixが与えられた場合、次のタイプの複数のクエリを処理します。

左上隅(row1, col1)と右下隅(row2, col2)で定義された長方形内のmatrixの要素の合計を計算します。
NumMatrixクラスを実装する：

NumMatrix(int[][] matrix)整数行列matrixでオブジェクトを初期化します。
int sumRegion(int row1, int col1, int row2, int col2)左上隅(row1, col1)と右下隅(row2, col2)で定義された長方形内のmatrixの要素の合計を返します。
sumRegionがO(1)時間計算量で動作するアルゴリズムを設計する必要があります。


"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return 
        H = len(matrix)
        W = len(matrix[0])
        
        #二次元累積和
        self.prefix = [[0] * (W+1) for _ in range(H+1)]
        
        for i in range(H):
            for j in range(W):
                self.prefix[i+1][j+1] = (
                    self.prefix[i][j+1]
                    + self.prefix[i+1][j]
                    - self.prefix[i][j]
                    + matrix[i][j]
                )
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return(
             self.prefix[row2+1][col2+1]
            - self.prefix[row1][col2+1]
            - self.prefix[row2+1][col1]
            + self.prefix[row1][col1]
        )
