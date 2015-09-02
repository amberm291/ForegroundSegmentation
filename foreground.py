import cv2
import numpy as np
import Queue
import sys

img = cv2.imread(sys.argv[1])
edgeImg = cv2.Canny(img,10,150)
kernel = np.ones((3,3),np.uint8)
grayDilated = cv2.dilate(edgeImg,kernel)
kernel = np.ones((2,2),np.uint8)
grayErode = cv2.erode(grayDilated,kernel)
floodOut = img
height,width = grayErode.shape[:2]
queue = Queue.Queue()
ref = grayErode[0][0]
visited = np.zeros((height,width))
queue.put([0,0])
queue.put([height-1,width-1])
queue.put([0, width-1])
queue.put([height-1,0])
#queue.put([0, width/2])
#queue.put([height-1, width/2])
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

cv2.imwrite('result.png',floodOut)
