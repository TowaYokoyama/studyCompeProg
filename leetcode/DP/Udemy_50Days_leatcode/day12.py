class Solution:
    def judgeCircle(self, moves: str) -> bool:
        #(右)、(左)、(上)、(下) = 'R''L''U''D'
        #原点に帰るならtrue,帰らないならfalse
         
        #origin 
        x = 0
        y = 0 
        for direction in moves:
            if direction == 'R':
                 x += 1
            elif direction == 'L':
                x -=1
            elif direction == 'U':
                y+=1
            else:y-=1
        
        return x == 0 and y == 0
         