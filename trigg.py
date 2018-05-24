import numpy as np
import cv2
import os
'''
 Life :
    live - 1
    dead - 0
'''
d=0
def rules(matrix,a,b):
    live=dead=status=0
    for i in [a-1,a,a+1]:
        for j in [b-1,b,b+1]:
            if matrix[i][j] == 1:
                live+=1
            elif matrix[i][j] == 0:
                dead+=1
    if live < 2 and matrix[a][b] == 1:
        status=0 #Any live cell with fewer than two live neighbors dies, as if by under population.
    elif matrix[a][b] == 1 and (live == 2 or live == 3):
        status=1 #Any live cell with two or three live neighbors lives on to the next generation.
    elif matrix[a][b] == 1 and live > 3:
        status=0 #Any live cell with more than three live neighbors dies, as if by overpopulation.
    elif matrix[a][b] == 0 and live ==3:
        status=1 #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    return (status)

def display(matrix):
    img = np.array(matrix ,dtype=np.uint8)
    #img = cv2.resize(img, (996, 996))
    retval, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    img = cv2.resize(img, (996, 996), interpolation=cv2.INTER_AREA )
    #cv2.imshow('trial',img)
    #cv2.waitKey(0)
    cv2.imwrite('/home/orange/gol/4/%s' %d + '.jpg',img)

def main():
    global d
    matrix = [[0,0,0,0,0,0,0,0],
              [0,0,1,0,0,1,0,0],
              [0,1,0,1,0,0,1,0],
              [0,0,0,0,1,0,1,0],
              [0,0,1,1,1,0,0,0],
              [0,0,0,1,0,0,0,0],
              [0,0,1,0,0,1,0,0],
              [0,0,0,0,0,0,0,0]]
    for iteration in range(0,200):
        for i in range(1,7):
            for j in range(1,7):
                matrix[i][j]=rules(matrix,i,j)
        display(matrix)
        #print(matrix)
        d+=1
    os.system("cd /home/orange/gol/4; ffmpeg -i %d.jpg -vcodec mpeg4 test.avi")
main()
