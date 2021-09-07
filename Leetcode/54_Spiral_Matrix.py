class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return matrix
        
        left = 0; right = len(matrix[0])-1
        top = 0; down = len (matrix)-1
        ans=[]
        while top <= down and left <= right:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
                
            for i in range(top+1, down+1):
                ans.append(matrix[i][right])
                
            for i in reversed(range(left, right)):
                if top == down:
                    break
                ans.append(matrix[down][i])
            
            for i in reversed(range(top +1, down)):
                if left == right:
                    break
                ans.append(matrix[i][left])
            
            top += 1
            down -= 1
            left += 1
            right -= 1
            
        return ans