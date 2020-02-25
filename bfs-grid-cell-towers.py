# 2.20.2020
#
# 2D grid of cell towers. All servers need to be updated to the latest
# software version. Servers that already have the update should not be
# updated again. Servers are in the form of a 2D array of 0 and 1 where the
# value 0 represents an outdated server and the value of 1 represents an
# updated server.
#
# In a single day, an updated server can push the update to each of its adjacent
# out of date servers.
#
# An adjacent server is either on the left, right, above or below a given server.
# Once the server receives the update, it becomes updated and can push the update
# to its adjacent servers on the following day.
#
# Given the 2D array representing the current status of the servers, write an
# algorithm that will determine the minimum number of days required to push the update
# to all available servers.

# Input:
# [[0, 1, 1, 0, 1],
#  [0, 1, 0, 1, 0],
#  [0, 0, 0, 0, 1],
#  [0, 1, 0, 0, 0]]
#
# Output: 2
#
# Explanation:
# At the end of the 1st day, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [0, 1, 0, 1, 1],
#  [1, 1, 1, 0, 1]]
#
# At the end of the 2nd second, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1]]

import unittest

def minDays(numRows, numCols, grid):
    if numRows == 0 or numCols == 0:
        return 0

    queue = [] # bfs.
    for i in range(numRows):
        for j in range(numCols):
            if grid[i][j] == 1:
                queue.append([i,j]) # append coordinates to queue if it holds an updated server.

    directions = [[0,-1], [0,1], [-1,0], [1,0]]
    days = 0

    if len(queue) == 0: # if there is no way we can update all servers, return -1.
        return -1

    while True:
        new_queue = []
        for [i,j] in queue: # loop through the coordinates containing updated servers.
            for d in directions:
                ni, nj = d[0] + i, d[1] + j # neighbor coordinates.
                # if the neighbor is a valid cell in the grid and is an outdated server.
                if 0 <= ni < numRows and 0 <= nj < numCols and grid[ni][nj] == 0:
                    grid[ni][nj] = 1 # update it.
                    new_queue.append([ni, nj]) # add the newly updated server to the new queue.

        # set the queue we are iterating to new_queue.
        queue = new_queue
        if len(queue) == 0:
            break
        days += 1

    if all(grid[i][j] == 1 for i in range(numRows) for j in range(numCols)):
        return days # if complete, return the number of days.
    else:
        return -1 # if we've reached the end and the grid cannot be fully updated, return -1.

class Test(unittest.TestCase):

    def test_one(self):
        numRows = 4
        numCols = 5
        grid = [[0, 1, 1, 0, 1],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0]]

        result = minDays(numRows, numCols, grid)
        expected = 2
        self.assertEqual(result, expected)

unittest.main(verbosity=2)
