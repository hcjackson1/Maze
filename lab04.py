#Lab04 main
from Stack import Stack



#North, then West, then South, then East

def print_maze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print(f"|{maze[row][col]:<2}", sep='',end='')
		print("|")


def maze_path_exists(maze, start_x, start_y):
    s1 = Stack()
    step = 1
    goal = False
    maze[start_x][start_y] = step
    s1.push((start_x, start_y))
    #print_maze(maze)
    step += 1
    while goal == False:
        #print(start_x)
        #print(start_y)
        if maze[start_x - 1][start_y] == 'G':
            return True
        if maze[start_x - 1][start_y] == ' ':
            #print('hi')
            s1.push((start_x - 1, start_y))
            maze[start_x - 1][start_y] = step
            step += 1
            start_x = start_x - 1
            
            #print_maze(maze)
            #print('')
            continue
        if maze[start_x][start_y - 1] == 'G':
            return True
        if maze[start_x][start_y - 1] == ' ':
            #print('yes')
            s1.push((start_x, start_y - 1))
            maze[start_x][start_y - 1] = step
            step += 1
            start_y = start_y - 1
            
            #print_maze(maze)
            #print('')
            continue
        if start_x + 1 <= len(maze[0]) - 1:
                if maze[start_x + 1][start_y] == 'G':
                    return True
                if maze[start_x + 1][start_y] == ' ':
                    s1.push((start_x + 1, start_y))
                    maze[start_x + 1][start_y] = step
                    step += 1
                    start_x = start_x + 1
            
            
                    #print(s1.items[0][0])
                    #print('')
                    continue
        if start_x + 1 <= len(maze) - 1:
                if maze[start_x][start_y + 1] == 'G':
                    return True
                if maze[start_x][start_y + 1] == ' ':
                    s1.push((start_x, start_y + 1))
                    maze[start_x][start_y + 1] = step
                    step += 1
                    start_y = start_y + 1

                    #print_maze(maze)
                    #print('')
                    continue
        #stack
        
        s1.pop()
        if s1.isEmpty() == True:
                #print('returning false')
                return False
        last = s1.peek()
        #maze[start_x][start_y] = step
        #step += 1
        start_x = last[0]
        start_y = last[1]
        #print(start_x)
        continue

        


'''
maze = [
    ['+','+','+','+','G','+'],
    ['+',' ','+',' ',' ','+'],
    ['+',' ',' ',' ','+','+'],
    ['+',' ','+','+',' ','+'],
    ['+',' ',' ',' ',' ','+'],
    ['+','+','+','+','+','+'] ]

#maze[2-1][3] = '6'
#print_maze(maze)

maze_path_exists(maze, 4,4)
'''
