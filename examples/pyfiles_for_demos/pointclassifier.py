### This function takes in three coordinate points as 1 x 2 nparrays and classifies them as the origin, x-axis max and y-axis max


def pointclassifier(userpoints):
    
    origin = []
    xaxismax = []
    yaxismax = []
    
    for i in range(len(userpoints)):

        ## origin
        if userpoints[i,0] == min(userpoints[:,0]) and userpoints[i,1] == max(userpoints[:,1]):
            print(userpoints[i,:], "is the pixel location of the origin")
            origin = userpoints[i,:]
    
        ## x max
        elif userpoints[i,0] == max(userpoints[:,0]):
            print(userpoints[i,:], "is the pixel location of the x-axis max")
            xaxismax = userpoints[i,:]
        
        ## y max point
        elif userpoints[i,0] == min(userpoints[:,0]) and userpoints[i,1] == min(userpoints[:,1]):
            print(userpoints[i,:], "is the pixel location of the y-axis max")
            yaxismax = userpoints[i,:]
        
        else:
            print(userpoints[i,:],"This point cannot be classified as one of the following: \n*Origin \n*X-coordinate max \n*y-coordinate max")
            break
    
    return origin, xaxismax, yaxismax