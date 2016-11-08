import cv2
import numpy as np
import Queue
import sys

def segmentImage(imgPath):
    '''
        PARAMETERS:
            imgPath (string): path of image to be extracted.
        OUTPUT:
            floodOut (numpy.ndarray): Output image with foreground extracted.
    '''

    img = cv2.imread(imgPath)

    '''Application of Canny Edge Detector'''
    edgeImg = cv2.Canny(img,10,120)
    #cv2.imwrite("images/canny.png",edgeImg)

    '''Dilation of canny output with a kernel of size (3x3)'''
    kernel = np.ones((3,3),np.uint8)
    grayDilated = cv2.dilate(edgeImg,kernel)
    #cv2.imwrite("images/dilate.png",grayDilated)

    '''Erosion of dilated image with a kernel of size (2x2)'''
    kernel = np.ones((2,2),np.uint8)
    grayErode = cv2.erode(grayDilated,kernel)
    #cv2.imwrite("images/eroded.png",grayErode)

    '''Breadth first search in the image to extract final output'''
    floodOut = img
    height,width = grayErode.shape[:2]
    queue = Queue.Queue()
    ref = grayErode[0][0]
    visited = np.zeros((height,width))
    queue.put([0,0])
    queue.put([height-1,width-1])
    queue.put([0, width-1])
    queue.put([height-1,0])

    while not queue.empty():
        a,b = queue.get()
        floodOut[a][b] = [0,0,0]
        if a>0 and b>0 and visited[a-1][b-1]==0:
            if grayErode[a-1][b-1] == ref:
                queue.put([a-1,b-1])
                visited[a-1][b-1]=1
            else:
                floodOut[a-1][b-1] = [0,0,0]
        if a>0 and visited[a-1][b]==0:
            if grayErode[a-1][b] == ref:
                queue.put([a-1,b])
                visited[a-1][b]=1
            else:
                floodOut[a-1][b] = [0,0,0]
        if b>0 and visited[a][b-1]==0:
            if grayErode[a][b-1] == ref:
                queue.put([a,b-1])
                visited[a][b-1]=1
            else:
                floodOut[a][b-1] = [0,0,0]
        if a>0 and b<(width-1) and visited[a-1][b+1]==0:
            if grayErode[a-1][b+1] == ref:
                queue.put([a-1,b+1])
                visited[a-1][b+1]=1
            else:
                floodOut[a-1][b+1] = [0,0,0]
        if b<(width-1) and visited[a][b+1]==0:
            if grayErode[a][b+1] == ref:
                queue.put([a,b+1])
                visited[a][b+1]=1
            else:
                floodOut[a][b+1] = [0,0,0]
        if a<(height-1) and b<(width-1) and visited[a+1][b+1]==0: 
            if grayErode[a+1][b+1] == ref:
                queue.put([a+1,b+1])
                visited[a+1][b+1]=1
            else:
                floodOut[a+1][b+1] = [0,0,0]
        if a<(height-1) and visited[a+1][b]==0:
            if grayErode[a+1][b] == ref:
                queue.put([a+1,b])
                visited[a+1][b]=1
            else:
                floodOut[a+1][b] = [0,0,0]
        if a<(height-1) and b>0 and visited[a+1][b-1]==0: 
            if grayErode[a+1][b-1] == ref:
                queue.put([a+1,b-1])
                visited[a+1][b-1]=1
            else:
                floodOut[a+1][b-1] = [0,0,0]

    return floodOut

if __name__=="__main__":
    imgPath = "images/input3.jpg"
    floodOut = segmentImage(imgPath)
    cv2.imwrite("images/result3p.png",floodOut)
