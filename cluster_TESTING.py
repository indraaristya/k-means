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

dataTrain = genfromtxt('testing.csv',delimiter=',') #testing.csv adalah file data test

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

xCent3 = (round(random.uniform(0,36),2))
yCent3 = (round(random.uniform(0,36),2))

xCent4 = (round(random.uniform(0,36),2))
yCent4 = (round(random.uniform(0,36),2))

xCent5 = (round(random.uniform(0,36),2))
yCent5 = (round(random.uniform(0,36),2))


# Code untuk melakukan random nilai sebagai centroid awal dari salah satu koordinat data latih
# xCent1 = random.choice(att1)
# yCent1 = random.choice(att2)
#
# xCent2 = random.choice(att1)
# yCent2 = random.choice(att2)
#
# xCent3 = random.choice(att1)
# yCent3 = random.choice(att2)
#
# xCent4 = random.choice(att1)
# yCent4 = random.choice(att2)
#
# xCent5 = random.choice(att1)
# yCent5 = random.choice(att2)

sumxC1 = 0
sumyC1 = 0
sumxC2 = 0
sumyC2 = 0
sumxC3 = 0
sumyC3 = 0
sumxC4 = 0
sumyC4 = 0
sumxC5 = 0
sumyC5 = 0

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

xCent = [xCent1,xCent2,xCent3,xCent4,xCent5]
yCent = [yCent1,yCent2,yCent3,yCent4,yCent5]
Cent = [xCent,yCent]
newCent = []
l = 1

while (Cent != newCent):
    sse = 0
    for i in range(0,100):
        # menghitung jarak setiap data ke setiap centroid
        clust1 = ecluiDistance(xCent1,yCent1,dataTrain[i,0],dataTrain[i,1])
        clust2 = ecluiDistance(xCent2,yCent2,dataTrain[i,0],dataTrain[i,1])
        clust3 = ecluiDistance(xCent3,yCent3,dataTrain[i,0],dataTrain[i,1])
        clust4 = ecluiDistance(xCent4,yCent4,dataTrain[i,0],dataTrain[i,1])
        clust5 = ecluiDistance(xCent5,yCent5,dataTrain[i,0],dataTrain[i,1])

        # menentukan data lebih dekat dengan centroid 1, 2, 3, 4 atau 5

        if (clust1 <= clust2):
            if (clust1 <= clust3):
                if (clust1 <= clust4):
                    if (clust1 <= clust5):
                        hasil[i,0] = clust1
                        hasil[i,1] = 1
        if (clust2 <= clust1):
            if (clust2 <= clust3):
                if (clust2 <= clust4):
                    if (clust2 <= clust5):
                        hasil[i, 0] = clust2
                        hasil[i, 1] = 2
        if (clust3 <= clust1):
            if (clust3 <= clust2):
                if (clust3 <= clust4):
                    if (clust3 <= clust5):
                        hasil[i, 0] = clust3
                        hasil[i, 1] = 3
        if (clust4 <= clust1):
            if (clust4 <= clust2):
                if (clust4 <= clust3):
                    if (clust4 <= clust5):
                        hasil[i, 0] = clust4
                        hasil[i, 1] = 4
        if (clust5 <= clust1):
            if (clust5 <= clust2):
                if (clust5 <= clust3):
                    if (clust5 <= clust4):
                        hasil[i, 0] = clust5
                        hasil[i, 1] = 5

    for i in range(0, 100):
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
        elif hasil[i,1] == 3:
            sumxC3 = sumxC3 + dataTrain[i,0]
            sumyC3 = sumyC3 + dataTrain[i,1]
            count3 = count3 + 1
            sse = sse + hasil[i,0]
        elif hasil[i,1] == 4:
            sumxC4 = sumxC4 + dataTrain[i,0]
            sumyC4 = sumyC4 + dataTrain[i,1]
            count4 = count4 + 1
            sse = sse + hasil[i,0]
        elif hasil[i,1] == 5:
            sumxC5 = sumxC5 + dataTrain[i,0]
            sumyC5 = sumyC5 + dataTrain[i,1]
            count5 = count5 + 1
            sse = sse + hasil[i,0]

    xCent = [xCent1, xCent2, xCent3, xCent4, xCent5]
    yCent = [yCent1, yCent2, yCent3, yCent4, yCent5]
    Cent = [xCent, yCent]

    # menentukan centroid baru dengan mencari rata-rata dari koordinat data pada setiap cluster
    xCent1 = round(sumxC1/count1,2)
    yCent1 = round(sumyC1/count1,2)

    xCent2 = round(sumxC2/count2,2)
    yCent2 = round(sumyC2/count2,2)

    xCent3 = round(sumxC3/count3,2)
    yCent3 = round(sumyC3/count3,2)

    xCent4 = round(sumxC4/count4,2)
    yCent4 = round(sumyC4/count4,2)

    xCent5 = round(sumxC5/count5,2)
    yCent5 = round(sumyC5/count5,2)

    xCent = [xCent1, xCent2, xCent3, xCent4, xCent5]
    yCent = [yCent1, yCent2, yCent3, yCent4, yCent5]
    newCent = [xCent,yCent]

    print("NewCent- ",l,": ",newCent)
    l = l+1

# xCent = [xCent1,xCent2,xCent3]
# yCent = [yCent1,yCent2,yCent3]
print("Cent X: ",xCent)
print("Cent Y: ",yCent)
print("SSE: ",sse)

#hasil prediksi di simpan pada file prediksiDataTest.txt
file = open('prediksiDataTest.txt', 'w')
for i in range(0,100):
    file.write(str(int(hasil[i,1])))
    file.write('\n')
file.close()

s=121
ax.scatter(xs=att1,ys=att2,c=hasil[:,1])
ax.scatter(xs=xCent, ys=yCent,s=2*s,c='red',marker='^',alpha=.8)
plot.show()
