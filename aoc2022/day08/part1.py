VIS = 0
if __name__ == '__main__':
    l = []
    with open("input.txt", 'r') as raw_in:
        #    with open("input_t.txt", 'r') as raw_in:
        data_in = raw_in.read().strip()

        lines = [x for x in data_in.split('\n')]
    print(lines)
    x = 0
    y = 0
    
    for i in lines:
        y += 1

    x = len(lines[0])
    print(f"length of lines: {x}")
    grid = []
    print(f"Number of rows(y): {y}, number of columns: {x}")
    for i in range(y):
        for j in range(x):
            grid.append([i, j])

    print(f"GRID {grid}")
    print(len(grid))
#    grid_d = { tuple(grid[i]):lines[grid[i][0]][grid[i][1]] for i in range(0, len(grid))}
#    print(f"GRID_D {grid_d}")
    for g in range(0, x):
        for h in range (0, y):
            vis_r = True 
            vis_l = True
            vis_n = True
            vis_s = True
            p = lines[g][h]
            #right  
            for m in range(h + 1, len(lines[g])):
                vis_r = False
                if lines[g][m] < p:
                    vis_r = True 
                else:
                    vis_r = False
                    break
            #left
            for m in range(0, h):
                vis_l = False
                if lines[g][m] < p:
                    vis_l = True 
                else:
                    vis_l = False
                    break
            #north
            for m in range(0, g):
                vis_n = False
                if lines[m][h] < p:
                    vis_n = True 
                else:
                    vis_n = False
                    break
            #south
            for m in range(g + 1, len(lines)):
                vis_s = False
                if lines[m][h] < p:
                    vis_s = True 
                else:
                    vis_s = False
                    break
            if vis_r  or vis_l  or vis_n or vis_s: 
                VIS += 1

    print(f"vis: {VIS}")
#    VIS = VIS + 2 * len(lines[0]) + 2 * len(lines) - 4
    print(f"visible nodes: {VIS}") 
