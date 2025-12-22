"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack:

    def __init__(self):
        self.stack = [] #通常のスタック
        self.min_stack = [] #最小値を追うstack

    def push(self, val: int) -> None:
        self.stack.append(val) #通常のスタックに値を追加
        
        #min_stackには新しい最小値を登録
        #まだ何もないなら、valを入れる
        #すでにあるなら、今のvalと前の最小値の小さいほうに入れる
        if not self.min_stack:
            
            self.min_stack.append(val)
            
        else:
            self.min_stack.append(min(val,self.min_stack[-1]))
    def pop(self) -> None:
        #どちらのstackからも削除(同時に動く)
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        #通常のstackの1番上を見る
        return self.stack[-1]
    def getMin(self) -> int:
        #min_stackの1番上が、今の全体の最小値
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()