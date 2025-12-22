class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        needed = 0
        people.sort() # 小さい順にソート
        left, right = 0, len(people)-1
        
        while left <= right:
            if(people[right] + people[left] <= limit):
                left += 1
            needed += 1
            right -= 1

        return needed
