"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
"""
#TC= for constructor n(log(n)) SC= O(1) constant k space
#TC= for add log(k) because adding and popping in heap is Log(n) complexity
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=nums
        self.k=k
        heapq.heapify(self.heap)#converts all the elements into heap 
        while(len(self.heap)>self.k):
            heapq.heappop(self.heap) 

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.k: #only remove if the length is gerater than 3
            heapq.heappop(self.heap)
        return self.heap[0]
#here, the smallest among the remaining 3 largest (because we removes all the elements from the heap(0) using heappop which deletes all the smallest elements and leaves the 3 largest)

                    


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

