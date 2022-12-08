VIS = 0
SCOR = 0
if __name__ == '__main__':
    l = []
    with open("input.txt", 'r') as raw_in:
        #    with open("input_t.txt", 'r') as raw_in:
        data_in = raw_in.read().strip()

        lines = [x for x in data_in.split('\n')]
    x = 0
    y = 0
    for i in lines:
        y += 1
    x = len(lines[0])
    grid = []
    for i in range(y):
        for j in range(x):
            grid.append([i, j])
    grid_d = { tuple(grid[i]):int(lines[grid[i][0]][grid[i][1]]) for i in range(0, len(grid))}
#    grid_d = { tuple(grid[i]):lines[grid[i][0]][grid[i][1]] for i in range(0, len(grid))}
#    print(f"GRID_D {grid_d}")
    for g in range(0, x):
        for h in range (0, y):
            vis_r, vis_l, vis_n, vis_s = True, True, True, True
            scor_r,scor_l, scor_n, scor_s = 0, 0, 0, 0 
            p = lines[g][h]
            grid_d[(g, h)] = 0
            #right  
            for m in range(h + 1, len(lines[g])):
                if lines[g][m] < p:
                    vis_r = True 
                else:
                    vis_r = False
                    break
            #left
            for m in range(0, h):
                if lines[g][m] < p:
                    vis_l = True 
                else:
                    vis_l = False
                    break
            #north
            for m in range(0, g):
                if lines[m][h] < p:
                    vis_n = True 
                else:
                    vis_n = False
                    break
            #south
            for m in range(g + 1, len(lines)):
                if lines[m][h] < p:
                    vis_s = True 
                else:
                    vis_s = False
                    break
            if vis_r  or vis_l  or vis_n or vis_s: 
                VIS += 1
            #right
            for m in range(h + 1, len(lines[g])):
                if lines[g][m] < p:
                    scor_r += 1
                elif lines[g][m] >= p:
                    scor_r += 1
                    break
            #left
            for m in range(h - 1, 0 - 1, -1):
                if lines[g][m] < p:
                    scor_l += 1
                elif lines[g][m] >= p:
                    scor_l += 1
                    break
            #north
            for m in range(g - 1, 0 - 1, -1) :
                if lines[m][h] < p:
                    scor_n += 1
                elif lines[m][h] >= p:
                    scor_n += 1
                    break
            #south
            for m in range(g + 1, len(lines)):
                if lines[m][h] < p:
                    scor_s += 1
                elif lines[m][h] >= p:
                    scor_s += 1
                    break
#           if scor_r == 0:
#               scor_r = 1
#           elif scor_l == 0:
#               scor_l = 1
#           elif scor_n == 0:
#               scor_n = 1 
#           elif scor_s == 0:
#               scor_s = 1
            scor = scor_r * scor_l * scor_n * scor_s
            if scor > SCOR:
                SCOR = scor
    print(f"visible nodes: {VIS}") 
    print(f"visibility Score {SCOR}")
