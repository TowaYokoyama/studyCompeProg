class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        countBinarySubstrings の Docstring
        
        :param self: 説明
        :param s: 説明
        :type s: str
        :return: 説明
        :rtype: int
        入力: s = "00110011"出力：6説明：「0011」、「01」、「1100」、「10」、「0011」、および「01」の連続した1と同じ数の部分文字列が6つあります。これらの部分文字列のいくつかは繰り返し、発生回数に応じてカウントされることに注意してください。また、「00110011」は、すべての0（および1）がグループ化されていないため、有効な部分文字列ではありません。
例2：

入力: s = "10101"出力：4説明：「10」、「01」、「10」、「01」の4つの部分文字列があり、連続した1と0の数が等しい。
        
        """
        rlu = []
        i = 0
        k = len(s)
        
        while i < k:
            j = i #jは最後尾
            while j<k and s[j] == s[i]:
                j+=1
            rlu.append((int(s[i]),j-i))#数字とその数字が出てきた個数
            i=j
            
        ans = 0
        for x in range(len(rlu)-1):#なんで-1するんやっけ x+1 がはみ出るのを防ぐため -1
            a,la = rlu[x]
            b,lb = rlu[x+1]
            
            #if b == a+1:
            ans += min(la,lb)
            """
                rlu = [
  ('0', 2),
  ('1', 2),
  ('0', 2),
  ('1', 2)
]
                """
             
        return ans