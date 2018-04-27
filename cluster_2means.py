#I Putu Indra Aristya - 1301154219

from numpy import genfromtxt, math
import numpy as np
import matplotlib.pyplot as plot
import random
from mpl_toolkits.mplot3d import Axes3D
fig = plot.figure()
ax = fig.add_subplot(111, projection='3d')

def ecluiDistance(a,b,x,y):
    return math.sqrt((a-x)**2) + ((b-y)**2)

dataTrain = genfromtxt('dataset.csv',delimiter=',') #dataset.csv adalah file data latih

att1 = dataTrain[:,0]
att2 = dataTrain[:,1]

#------Code untuk visualisasi data latih dengan scatter plot------
# ax.scatter(xs=att1, ys=att2) # plot 3D
# plot.plot(att1,att2,'bo') #plot 2D
# plot.show()

hasil = dataTrain*0

# Code untuk melakukan random nilai sebagai centroid awal dari rentang 0 - 36 dan dibulatkan 2 angka di belakang koma
xCent1 = (round(random.uniform(0,36),2))
yCent1 = (round(random.uniform(0,36),2))

xCent2 = (round(random.uniform(0,36),2))
yCent2 = (round(random.uniform(0,36),2))

# Code untuk melakukan random nilai sebagai centroid awal dari salah satu koordinat data latih
# xCent1 = random.choice(att1)
# yCent1 = random.choice(att2)
#
# xCent2 = random.choice(att1)
# yCent2 = random.choice(att2)


sumxC1 = 0
sumyC1 = 0
sumxC2 = 0
sumyC2 = 0

count1 = 0
count2 = 0


xCent = [xCent1,xCent2]
yCent = [yCent1,yCent2]
Cent = [xCent,yCent]
newCent = []
l = 1

while (Cent != newCent):
    sse = 0
    for i in range(0,688):
        # menghitung jarak setiap data ke setiap centroid
        clust1 = ecluiDistance(xCent1,yCent1,dataTrain[i,0],dataTrain[i,1])
        clust2 = ecluiDistance(xCent2,yCent2,dataTrain[i,0],dataTrain[i,1])

        # menentukan data lebih dekat dengan centroid 1 atau 2
        if (clust1 <= clust2):
            hasil[i,0] = clust1
            hasil[i,1] = 1
        if (clust2 <= clust1):
            hasil[i, 0] = clust2
            hasil[i, 1] = 2

    for i in range(0, 688):
        # menjumlahkan koordinat data di setiap cluster untuk mempermudah pencarian centroid baru
        if hasil[i,1] == 1:
            sumxC1 = sumxC1 + dataTrain[i,0]
            sumyC1 = sumyC1 + dataTrain[i,1]
            count1 = count1 + 1
            sse = sse + hasil[i,0]
        elif hasil[i,1] == 2:
            sumxC2 = sumxC2 + dataTrain[i,0]
            sumyC2 = sumyC2 + dataTrain[i,1]
            count2 = count2 + 1
            sse = sse + hasil[i,0]

    xCent = [xCent1, xCent2]
    yCent = [yCent1, yCent2]
    Cent = [xCent, yCent]

    # menentukan centroid baru dengan mencari rata-rata dari koordinat data pada setiap cluster
    xCent1 = round(sumxC1/count1,2)
    yCent1 = round(sumyC1/count1,2)

    xCent2 = round(sumxC2/count2,2)
    yCent2 = round(sumyC2/count2,2)

    xCent = [xCent1, xCent2]
    yCent = [yCent1, yCent2]
    newCent = [xCent,yCent]

    print("NewCent- ",l,": ",newCent)
    l = l+1


# xCent = [xCent1,xCent2,xCent3]
# yCent = [yCent1,yCent2,yCent3]
print("Cent X: ",xCent)
print("Cent Y: ",yCent)
print("SSE: ",sse)

s=121
ax.scatter(xs=att1,ys=att2,c=hasil[:,1])
ax.scatter(xs=xCent, ys=yCent,s=2*s,c='red',marker='^',alpha=.8)
plot.show()
