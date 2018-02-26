from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]


matrix1 = [ [1,2,3,4] , [5,6,7,8] , [9,1,1,1] , [7,7,7,7]]
matrix2 = [ [1,1,1,1] ,[1,1,1,1], [1,1,1,1], [1,1,1,1]]

print "MATRIX1:"
print_matrix( matrix1)
print ""
print "MATRIX2:"
print_matrix(matrix2)
print "\nPRODUCT:"
print_matrix(matrix_mult(matrix1, matrix2))

identity = new_matrix()
ident(identity)
print_matrix(identity)


matrix = new_matrix()

add_edge(matrix, 125, 375, 0, 375, 375, 0)
add_edge(matrix, 125, 375, 0, 125, 250, 0)
add_edge(matrix, 125, 250, 0,375, 250, 0)
add_edge(matrix,375,250, 0, 375, 125, 0)
add_edge(matrix, 125, 125, 0,  375,125, 0)
add_edge(matrix, 225, 400, 0,225,100, 0)
add_edge(matrix, 275, 400, 0,275,100, 0)


draw_lines(matrix,screen,color)



save_ppm(screen, 'img.ppm')
