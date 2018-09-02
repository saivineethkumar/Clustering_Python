'''
Author: Dara Sai Vineeth Kumar
Roll no: 15EC35012
Course subject: MIES
Assignment: 1 - Clustering
'''


#Importing libraries
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

#Importing dataset and Storing the data
dataset = pd.read_excel('dataset.xlsx', header=None)
X=list(dataset.iloc[:,0].values)
Y=list(dataset.iloc[:,1].values)
maxx=int(max(X))
maxy=int(max(Y))


#Functions:
#Euclidean distance between two points
def dist(p1,p2):
    return ( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )**0.5

#Centroid of a set of points
def avgpt(ptl):
    ptx=[]
    pty=[]
    for pt in ptl:
        ptx.append(pt[0])
        pty.append(pt[1])
    return [np.mean(ptx), np.mean(pty)]

#Sum of distances from a point to set of points
def cendist(p1,pl):
    flag=0
    for pt in pl:
        flag+= dist(p1,pt)

    return flag


#main function
errlist=[]
cenpts3=[]

for k in range(1,6):


    if k==1:
        cenX = np.mean(X)
        cenY = np.mean(Y)
        error=0
        for i in range(len(X)):
            error=error+dist( [cenX,cenY] , [X[i],Y[i]] )
        error=round(error/len(X),2)
        errlist.append(error)
        print('For k = {} error = {}'.format(k,error))

    else:
        cen = [[random.randint(0,maxx),random.randint(0,maxy)] for _ in range(k)]
        while(1):
            newcen=[]
            cenpts=[[] for _ in range(k)]
            for i in range(len(X)):
                cendis=[]
                for pt in cen:
                    cendis.append(dist(pt, [ X[i],Y[i] ] ))
                cenpts[ cendis.index(min(cendis)) ].append([ X[i],Y[i] ])

            for index,ptlist in enumerate(cenpts):
                if len(ptlist) ==0:
                    newcen.append(cen[index])
                else:
                    newcen.append(avgpt(ptlist))
            if newcen==cen:
                break
            else:
                cen[:]=newcen[:]

        error=0
        for i in range(len(newcen)):
            error = error + cendist(newcen[i], cenpts[i])

        if k==3:
            cenpts3[:]=cenpts[:]

        error= round(error/len(X),2)
        errlist.append(error)
        print('For k = {} error = {}'.format(k,error))


#printing k and corresponding error
#print(list(zip(range(1,6), errlist) ))


#Plot for Error vs k
plt.plot(range(1,6), errlist, linestyle='-', marker='o')
plt.title('Avarage errror Vs number of clusters k')
plt.xlabel('k')
plt.ylabel('error')
plt.show()


#Visualization of given dataset
plt.scatter(X,Y, marker='.' )
plt.title('Dataset visualization - points(x,y)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


#Visualization of given dataset at elbow point k=3 (since we found out that 3 is elbow point):
a = np.array(cenpts3[0])
b = np.array(cenpts3[1])
c = np.array(cenpts3[2])

plt.scatter(a[:,0], a[:,1], c='r', marker='.')
plt.scatter(b[:,0], b[:,1], c='m', marker='.')
plt.scatter(c[:,0], c[:,1], c='c', marker='.')
plt.title('Dataset visualization for k=3')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
