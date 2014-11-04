import numpy as np
from numpy import genfromtxt, sqrt
my_data = genfromtxt('sudoku_in_1_moderate.csv', delimiter=',')
n=sqrt(my_data.shape)
m=sqrt(n)
unsolved_array= my_data.reshape((n,n))#numpy array
unsolved=unsolved_array.tolist()#convert numpy_array to list
my_sudoku=dict()
i=0

for q in unsolved:#takes a row or single list in q at a time
    for j in range(len(q)):
        my_sudoku[(i, j)] = unsolved[i][j]
    i+=1

def rule1(sudoku,n):
    m=sqrt(n)
    for i in range(n):
        for j in range(n):
            if type(sudoku[(i,j)])==type([]):
                if len(sudoku[(i,j)])==1:
                    b=sudoku[(i,j)][0]
                    del sudoku[(i,j)]
                    sudoku[(i,j)]=b
    sudoku=find_poss(sudoku)
    return sudoku

def find_poss(sudoku):
    for p in range(0,m):
        for q in range(0,m):
            for i in range(p*m, p*m+m):        
                for j in range(q*m, q*m+m):
                    if my_sudoku[(i,j)]==0 or type(my_sudoku[(i,j)])==type([]):
                        my_sudoku[(i,j)]=[]
                        for a in range(1,n+1):
                            if a not in dict(((i,y),my_sudoku[(i,y)]) for y in range(n)).values():
                                if a not in dict(((y,j),my_sudoku[(y,j)]) for y in range(n)).values():
                                    flag=0
                                    for k in range(p*m, p*m+m):
                                        for l in range(q*m, q*m+m):
                                            if a == my_sudoku[(k,l)]:
                                                flag=1
                                    if flag ==0:
                                        my_sudoku[(i,j)].append(a)
    return sudoku

my_sudoku=find_poss(my_sudoku)
print sorted(my_sudoku.items())

def rule2(sudoku,n):
    m=sqrt(n)
    not_in_row=0
    not_in_col=0
    not_in_box=0
    for p in range(0,m):
        for q in range(0,m):
            for i in range(p*m, p*m+m):       
                for j in range(q*m, q*m+m):
                    if type(sudoku[(i,j)])==type([]):#taking a list of candidates
                        (sudoku[(i+1000,j+1000)])=(sudoku[(i,j)])
                        (sudoku[(i,j)])=0
                        for b in sudoku[(i+1000,j+1000)]:#taking each element
                            for y in range(n):#loop for row
                                not_in_row=0
                                if type(sudoku[(i,y)])==type([]):
                                    if b not in sudoku[(i,y)]:
                                        not_in_row=1
                            for y in range(n):
                                not_in_col=0
                                if type(sudoku[(y,j)])==type([]):
                                    if b not in sudoku[(y,j)]:
                                        not_in_col = 1
                            for k in range(p*m, p*m+m):
                                for l in range(q*m, q*m+m):
                                    not_in_box=0
                                    if type(sudoku[(k,l)])==type([]):
                                        if b not in sudoku[(k,l)]:
                                            not_in_box=1
                        if not_in_box==1 and not_in_col==1 and not_in_row==1:
                            rule2_res=b
                            sudoku[(i,j)]=rule2_res
                        else: sudoku[(i,j)] = sudoku[(i+1000,j+1000)]
                        del sudoku[(i+1000,j+1000)]
    sudoku=find_poss(sudoku)
    return sudoku
# Apply RULE 1
for i in range(n):
    for j in range(n):
#         if type(my_sudoku[(i,j)])==type(2.0):
#             my_sudoku[(i,j)]=int(my_sudoku[(i,j)])
        if type(my_sudoku[(i,j)])==type([]):
            my_sudoku=rule1(my_sudoku, n)
print sorted(my_sudoku.items())
my_sudoku=rule2(my_sudoku,n)
print sorted(my_sudoku.items())
for i in range(n):
    for j in range(n):
#         if type(my_sudoku[(i,j)])==type(2.0):
#             my_sudoku[(i,j)]=int(my_sudoku[(i,j)])
        if type(my_sudoku[(i,j)])==type([]):
            my_sudoku=rule1(my_sudoku, n)
print sorted(my_sudoku.items())
def rule3(sudoku,n):
    for p in range(0,m):
        for q in range(0,m):
            for i in range(p*m, p*m+m):       
                for j in range(q*m, q*m+m):
                    temp=[]    
                    if type(sudoku[(i,j)])==type([]) and len(sudoku[(i,j)])==2:# got a pair
                        sudoku[(i+1000,j+1000)] = sudoku[(i,j)]
                        sudoku[(i,j)]=0#removed the pair from there
                        if sudoku[(i+1000,j+1000)] in dict(((i,y),my_sudoku[(i,y)]) for y in range(n)).values():#checking for same pair in the row
                                            #if there is same pair in the row
                            for y in range(n):#traversing the row element-wise
                                if sudoku[(i+1000,j+1000)] == sudoku[(i,y)]:
                                    sudoku[(i+1000,y+1000)] = sudoku[(i+1000,j+1000)]
                                    sudoku[(i,y)]=0#remove that pair also from that place
                                    for b in sudoku[(i+1000,j+1000)]:#now take each element of the array
                                        for x in range(n):#
                                            if type(sudoku[(i,x)])==type([]) and b in sudoku[(i,x)]:# checking each array row-wise
                                                sudoku[(i,x)].remove(b)#removing the element from each array
                                    sudoku[(i,y)]=sudoku[(i+1000,y+1000)]
                                    del sudoku[(i+1000,y+1000)]
                                               
                        if sudoku[(i+1000,j+1000)] in dict(((y,j),my_sudoku[(y,j)]) for y in range(n)).values():# checking for the pair in column
                            for y in range(n):#traversing the row element-wise
                                if sudoku[(i+1000,j+1000)] == sudoku[(y,j)]:
                                    sudoku[(y+1000,j+1000)] = sudoku[(i+1000,j+1000)]
                                    sudoku[(y,j)]=0#remove that pair also from that place
                                    for b in sudoku[(i+1000,j+1000)]:#now take each element of the array
                                        for x in range(n):
                                            if type(sudoku[(x,j)])==type([]) and b in sudoku[(x,j)]:# checking each array column-wise
                                                sudoku[(x,j)].remove(b)#removing the element from each array
                                    sudoku[(y,j)]=sudoku[(y+1000,j+1000)]
                                    del sudoku[(y+1000,j+1000)]
                        for k in range(p*m, p*m+m):
                            for l in range(q*m, q*m+m):
                                if sudoku[(k,l)]==sudoku[(i+1000,j+1000)]:
                                    sudoku[(k+1000,l+1000)] = sudoku[(i+1000,j+1000)]
                                    sudoku[(k,l)]=0#remove that pair also from that place
                                    for b in sudoku[(i+1000,j+1000)]:#now take each element of the array
                                        for x in range(p*m, p*m+m):
                                            for z in range(q*m, q*m+m):
                                                if type(sudoku[(x,z)])==type([]) and b in sudoku[(x,z)]:# checking each array column-wise
                                                    sudoku[(x,z)].remove(b)#removing the element from each array
                                    sudoku[(k,l)]=sudoku[(k+1000,l+1000)]
                                    del sudoku[(k+1000,l+1000)]
                        sudoku[(i,j)] = sudoku[(i+1000,j+1000)]
                        del sudoku[(i+1000,j+1000)]    
    return sudoku
for i in range(n):
    for j in range(n):
#         if type(my_sudoku[(i,j)])==type(2.0):
#             my_sudoku[(i,j)]=int(my_sudoku[(i,j)])
        if type(my_sudoku[(i,j)])==type([]):
            my_sudoku=rule1(my_sudoku, n)
            my_sudoku=rule3(my_sudoku, n)
            my_sudoku=rule1(my_sudoku, n)
print sorted(my_sudoku.items())
#print np.asarray(semi_solved_array)
