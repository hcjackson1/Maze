#Lab04 testFile
from lab04 import maze_path_exists
from lab04 import print_maze
from Stack import Stack

def test_example():
	maze = [
    ['+','+','+','+','G','+'],
    ['+',' ','+',' ',' ','+'],
    ['+',' ',' ',' ','+','+'],
    ['+',' ','+','+',' ','+'],
    ['+',' ',' ',' ',' ','+'],
    ['+','+','+','+','+','+'] ]
	assert maze_path_exists(maze, 4, 4) == True

	assert maze == [
    ['+', '+', '+', '+', 'G', '+'],
    ['+', 8, '+', 11, 12, '+'],
    ['+', 7, 9, 10, '+', '+'],
    ['+', 6, '+', '+', 2, '+'],
    ['+', 5, 4, 3, 1, '+'],
    ['+', '+', '+', '+', '+', '+'] ]
	maze2 = [['+','+','+','+','+','+','+','+'],
        ['+',' ',' ',' ',' ',' ','G','+'],
        ['+',' ',' ',' ',' ',' ',' ','+'],
        ['+',' ',' ',' ',' ',' ',' ','+'],
        ['+',' ',' ',' ',' ',' ',' ','+'],
        ['+',' ',' ',' ',' ',' ',' ','+'],
        ['+','+','+','+','+','+','+','+']]
	assert maze_path_exists(maze2, 5, 5) == True
	
	maze3 = [
    ['+','G','+'],
    [' ','+','+'],
    [' ',' ','+']]
	assert maze_path_exists(maze3, 2,1) == False
	assert maze3 == [
    ['+','G','+'],
    [3,'+','+'],
    [2,1,'+']]

	maze4 = [
    ['+','G','+'],
    [' ',' ','+'],
    [' ',' ','+']]
	assert maze_path_exists(maze4, 2,1) == True
	assert maze4 == [
    ['+','G','+'],
    [' ',2,'+'],
    [' ',1,'+']]
	
	

	
	



test_example()

maze = [
    ['+','G','+'],
    [' ','+','+'],
    [' ',' ','+']]
#maze[2-1][3] = '6'
#print_maze(maze)

#maze_path_exists(maze, 2,1)

