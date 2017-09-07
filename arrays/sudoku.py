# Arrays
# from codefights 
# by oz


def sudoku2(grid):
    #checking row
    for row in grid:
        if not rowCheck(row):
            print "row ",row
            return False
    #checking col
    for i in range(0,9):
        col=[]
        for j in range(0,9):
            #print j,i
            col.append(grid[j][i])
           
        if not rowCheck(col):
            print "col",col
            return False
    
    #checking square
    if not rowCheck(squarez(0,3,0,3,grid)):
        return False
    
    if not rowCheck(squarez(0,3,3,6,grid)):
        return False
    
    if not rowCheck(squarez(0,3,6,9,grid)):
        return False
    
    if not rowCheck(squarez(3,6,0,3,grid)):
        return False
    
    if not rowCheck(squarez(3,6,3,6,grid)):
        return False
    
    if not rowCheck(squarez(3,6,6,9,grid)):
        return False
    
    if not rowCheck(squarez(6,9,0,3,grid)):
        return False
    
    if not rowCheck(squarez(6,9,3,6,grid)):
        return False
    
    if not rowCheck(squarez(6,9,6,9,grid)):
        return False
    
    
    
    
    
    
    return True

def squarez(x,y,x1,y1,grid):
    squarelist=[]
    for i in range(x,y):
        for j in range(x1,y1):
            #print " ",i,j,
            squarelist.append(grid[i][j])
        
        #print ""
    return squarelist

def rowCheck(r):
    nums=[0 for x in range(1,10)]
    
    for num in r:
        if num != '.':
            #print num
            nums[int(num)-1]+=1
            if nums[int(num)-1]==2:
                print "failed",nums[int(num)-1]
                return False
        
    return True

    
                
                