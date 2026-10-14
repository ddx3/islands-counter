# Counting islands

Task 1 from the test assignment. There is a map M x N, where 1 is land and 0 is ocean.
The goal is to count the islands.

## How I understood the task

An island is a group of land cells connected by sides (up, down, left, right).
Cells that touch only by a corner are not connected. This follows from the examples:
in the second example three ones stand on a diagonal and the answer is 3, but if the
diagonal counted, it would be 1. The third example is the same: the answer is 2, and with
diagonals it would be 1.

## How to run

Only Python 3 is needed, nothing to install.

    python islands.py

Enter M and N in the first line, then M lines with N numbers separated by spaces. For example:

    3 4
    0 0 0 1
    0 0 1 1
    0 1 0 1

The answer will be 2. The input can also come from a file: `python islands.py < input.txt`

## How it works

The program goes through all cells. When it finds land, it increases the counter and walks
through the whole island with depth-first search (DFS). Every visited cell is set to 0, so it
is not counted twice. DFS is done with a stack and not with recursion, otherwise a big map
can exceed the recursion limit.

Every cell goes into the stack at most once, so the running time is O(M * N). There is no
separate matrix for visited cells, zeros are written into the input matrix itself. The
downside is that `count_islands` changes the matrix that was passed to it.

## Tests

    python test_islands.py

There are the three examples from the task and a few more cases of my own: an empty map,
only land, a chessboard (diagonals are not connected), a lake with an island inside and a
long snake.
