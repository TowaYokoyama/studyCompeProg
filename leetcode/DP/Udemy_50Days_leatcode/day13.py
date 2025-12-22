class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        テストケース
        Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
        """
        int_a = int(a, 2)
        int_b = int(b, 2)

        # 足し算
        total = int_a + int_b

        # 結果を2進数文字列に戻して '0b' を消す
        return bin(total)[2:]
    
    
class Solution:
    def addBinary(self, a: str, b:str) -> str:
        result = [] #結果を入れるリスト
        i, j = len(a) -1, len(b) -1 #右端からスタート
        carry = 0 #繰り上がり
        
        while i >= 0 or j >=0 or carry:
            total = carry #前の繰り上がりを足す
            
            if i >=0:
                total +=int(a[i])
                i-=1
            if j >= 0:
                total += int(b[j])
                j-=1
                
            result.append(str(total %2))
            
            carry = total //2 
        return ''.join(reversed(result))