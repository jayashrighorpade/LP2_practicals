g=0
def print_board(elements):
    for i in range(9):
        if i%3 == 0:
            print()
        if elements[i]==-1:
            print("_", end = " ")
        else:
            print(elements[i], end = " ")
    print()

def solvable(start): #check if puzzle is solvab;e even = solvebale, odd=not solvalbe no of inversions
    inv=0 # if smaller num comes after greater num i.e 7,5 five comes after 7
    #if there are even num of inversion then matrix is solvabe else puzzle is not solvable

    for i in range(9):
        if start[i] <= 1:
            continue # ignored -1
        for j in range(i+1,9):
            if start[j]==-1:
                continue # ignored -1
            if start[i]>start[j]:
                inv+=1
    if inv%2==0:
        return True
    return False

def heuristic(start,goal):
    global g
    h = 0
    for i in range(9):
        for j in range(9):
            if start[i] == goal[j] and start[i] != -1:
                h += (abs(j-i))//3 + (abs(j-i))%3  #to caluclate the disctance of the time from its original place in terms of rows and cols
    return h + g

def moveleft(start,position):
    start[position],start[position-1]= start[position-1],start[position]

def moveright(start,position):
    start[position],start[position+1]= start[position+1],start[position]

def moveup(start,position):
    start[position],start[position-3]= start[position-3],start[position]

def movedown(start,position):
    start[position],start[position+3]= start[position+3],start[position]


def movetile(start,goal):
    emptyat= start.index(-1)  # Finding index of -1
    row = emptyat//3 #finding which row and col the -1 is situated if we convert the lint into 2d matrix
    col = emptyat%3

    t1,t2,t3,t4 = start[:],start[:],start[:],start[:] #check tge combinatuon possibilits
    f1,f2,f3,f4 = 100,100,100,100

    if col-1 >= 0:
        moveleft(t1, emptyat)
        f1 = heuristic(t1, goal)
    if col+1 < 3:
        moveright(t2, emptyat)
        f2 = heuristic(t2, goal)
    if row + 1 < 3:
        movedown(t3, emptyat)
        f3 = heuristic(t3, goal)
    if row-1 >= 0 :
        moveup(t4, emptyat)
        f4 = heuristic(t4, goal)
    
    
    min_heuristic = min(f1, f2, f3, f4)

    if f1==min_heuristic:
        moveleft(start, emptyat)
    elif f2==min_heuristic:
        moveright(start, emptyat)
    elif f3==min_heuristic:
        movedown(start, emptyat)
    elif f4 == min_heuristic:
        moveup(start, emptyat)
        
        
def solveEight(start,goal):
    global g
    g+=1
    movetile(start,goal)
    print_board(start)
    f = heuristic(start,goal)
    if f == g:
        print(f"\nSolved in {f} moves")
        return
    solveEight(start,goal)


# global g
# start = list()
# goal = list()
# print("Enter the start state:(Enter -1 for empty):")
# for i in range(9):
#     start.append(int(input()))
# print("Enter the goal state:(Enter -1 for empty):")
# for i in range(9):
#     goal.append(int(input()))

start = [1, 2, 3, -1, 4, 6, 7, 5, 8]
# start = [1, 2, 3, 4, 5, 6, -1, 8, 7]
goal = [1, 2, 3, 4, 5, 6, 7, 8, -1]

print('Start state')
print_board(start)
print("----------------------------------------------- ")

# To check if solvable
if solvable(start):
    solveEight(start,goal)
    # print("Solved in {} moves".format(g))
else:
    print("Not possible to solve")