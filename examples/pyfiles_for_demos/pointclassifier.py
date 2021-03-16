### This function takes in three coordinate points as 1 x 2 nparrays and classifies them as the origin, x-axis max and y-axis max

import math


def pointclassifier(userpoints):
    

    origin = []
    xpixelmax = []
    ypixelmax = []
    

    for i in range(len(userpoints)):

        ## classify which pixel point is the origin
        if math.isclose(userpoints[i,0], min(userpoints[:,0]), rel_tol = 0.15 ) == True and math.isclose(userpoints[i,1], max(userpoints[:,1]), rel_tol = 0.15) == True:
            print(userpoints[i,:], "is the pixel location of the origin")
            origin = userpoints[i,:]
        
        ## classify which pixel point is the y max point on the y-axis coordinate
        elif math.isclose(userpoints[i,0], min(userpoints[:,0]), rel_tol = 0.15 ) == True and math.isclose(userpoints[i,1], min(userpoints[:,1]), rel_tol = 0.15 ) == True:
            print(userpoints[i,:], "is the pixel location of the y-axis max")
            ypixelmax = userpoints[i,:]
        
        ## classify which pixel point is the x max point on the x-axis coordinate
        elif math.isclose(userpoints[i,0], max(userpoints[:,0]), rel_tol = 0.15 ) == True:
            print(userpoints[i,:], "is the pixel location of the x-axis max")
            xpixelmax = userpoints[i,:]

        else:
            print(userpoints[i,:],"This point cannot be classified as one of the following: \n*Origin \n*X-coordinate max \n*y-coordinate max")
            print("Please read notes and try selecting the points again")
            break
    

    return origin, xpixelmax, ypixelmax