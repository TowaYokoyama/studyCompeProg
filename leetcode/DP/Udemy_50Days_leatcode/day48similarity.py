"""
You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.
Example 1:

Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes "03:30".
- Add 60 minutes to current. current becomes "04:30".
- Add 5 minutes to current. current becomes "04:35".
It can be proven that it is nopossible to convert current to correct in fewer than 3 operations.
Example 2:

Input: current = "11:00", correct = "11:01"
Output: 1
Explanation: We only have to add one minute to current, so the minimum number of operations needed is 1.
"""
#貪欲法
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        #分単位に変換
        def to_minutes(time_str: str) -> int:
            hours, minutes = time_str.split(":")
            return int(hours) * 60 + int(minutes)

        to_current = to_minutes(current)
        to_correct = to_minutes(correct)
        diff = to_correct - to_current
        answer = 0
        #1分と5分と15分と60分       
        while diff > 0:

            if diff >= 60:
                diff -= 60
                answer +=1

            elif 15<= diff <60:
                diff -= 15
                answer +=1

            elif 5<= diff < 15:
                diff -= 5
                answer += 1
            
            else:
                diff -= 1
                answer+=1

        return answer
    
