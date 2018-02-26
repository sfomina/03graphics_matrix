import math


def print_matrix( matrix ):
    counter = 0
    ans = ""
    while counter < len(matrix[0]):
        for col in matrix:
            ans +=  str(col[counter]) + " "
        ans += "\n"
        counter += 1
    print ans

def ident( matrix ):
    counter = 0
    for col in matrix:
        col[counter] = 1
        counter += 1

#m1 * m2 -> m3
def matrix_mult( m1, m2 ):
    m3 = new_matrix()
    for i in range(len(m1[0])):
        for y in range(len(m2)):
            sum = 0
            x = 0
            for l in m1:
                sum += l[i] * m2[y][x]
                x+=1
            m3[y][i] = sum 
            #print sum
    return m3
            
        


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m


'''
matrix = [ [1,2,3,4] , [5,6,7,8] , [9,1,1,1] , [7,7,7,7]]
matrix2 = [ [1,1,1,1] ,[1,1,1,1], [1,1,1,1], [1,1,1,1]]
ident(matrix2)
print "MATRIX1:"
print_matrix( matrix)
print ""
print "MATRIX2:"
print_matrix(matrix2)
print "\nPRODUCT:"
print_matrix(matrix_mult(matrix, matrix2))
'''

#print_matrix(new_matrix())
#ident(matrix)
#print_matrix(matrix)

