#https://practice.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab
class TwoStacks:
    def __init__(self, n=100):
        self.size = n
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = n

    # Function to push an integer into stack 1
    def push1(self, x):
        if self.top1<self.top2-1:
            self.top1+=1
            self.arr[self.top1]=x
    # Function to push an integer into stack 2
    def push2(self, x):
        if self.top1<self.top2-1:
            self.top2-=1
            self.arr[self.top2]=x

    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.top1<self.size and self.top1>=0:
            val = self.arr[self.top1]
            self.top1-=1
            return val
        return -1

    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.top2>=0 and self.top2<self.size:
            val = self.arr[self.top2]
            self.top2+=1
            return val
        return -1