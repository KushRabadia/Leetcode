class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        land = set()
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    land.add((row, column))
        islands = 0

        def explore(r, c):
            if (r,c) in land:
                land.remove((r,c))
                explore(r, c+1)
                explore(r, c-1)
                explore(r+1, c)
                explore(r-1, c)            

        while land:
            piece = land.pop()
            land.add(piece)

            explore(piece[0], piece[1])
            islands += 1

        return islands
