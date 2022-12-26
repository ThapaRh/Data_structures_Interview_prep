"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""
#TC=Log(m*n) SC=O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_start=0
        row_end=len(matrix)-1
        target_row=-1
        col=len(matrix[0])-1
        while(row_start<=row_end):
            mid=(row_end+row_start)//2
            if target<matrix[mid][0]:
                row_end=mid-1
            elif target>matrix[mid][col]:
                row_start=mid+1
            else:
                target_row=mid
                break
        print(target_row)
        #First find the row in which the target lies 
        #Then the search within the row if there is that element 
        #All via binary search
        if target_row==-1:
            return False
        else:
            start=0
            end=col
            while(start<=end):
                mid=(start+end)//2
                if matrix[target_row][mid]>target:
                    end=mid-1
                elif matrix[target_row][mid]<target:
                    start=mid+1
                elif matrix[target_row][mid]==target:
                    return True
            return False
        