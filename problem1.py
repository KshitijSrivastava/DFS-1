
## Problem1 (https://leetcode.com/problems/flood-fill/)


class Solution:
    def isInsideImage(self, nrows, ncols, i, j):
        """ To find if the position is inside the image """
        return i >= 0 and i < nrows and j >= 0 and j < ncols 
        pass
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #find the number of rows and columns
        nrows = len(image)
        ncols = len(image[0])
        
        #2d array to keep track of visited nodes
        visited = []
        for i in range(nrows):
            visited.append( [ False for j in range(ncols) ] )
        
        #storing the old colro
        oldColor = image[sr][sc]
        
        #stack
        stack = []
        stack.append( (sr,sc) )
        #making the staring node as visited
        visited[sr][sc] = True
        
        while len(stack) != 0:
            pos = stack.pop()
            
            #making the point to the new color
            i, j = pos[0], pos[1]
            image[i][j] = newColor
            
            #interating over all the possible directions
            for dx, dy in [ (0,1), (1, 0), (0, -1), (-1, 0) ]:
                new_i = i + dx
                new_j = j + dy
                
                #if inside the image, not visited and image point color is equal to old color
                if self.isInsideImage(nrows, ncols, new_i, new_j) and \
                visited[new_i][new_j] == False and image[new_i][new_j] == oldColor:
                
                    stack.append( (new_i, new_j) )
                    visited[new_i][new_j] = True
                    
        return image