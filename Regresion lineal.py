import statistics
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



edades =[
        44,
        46,
        42,
        57,
        21,
        65,
        47,
        51,
        65,
        70,
        19,
        22,
        39,
        48,
        56,
        65,
        42,
        56,
        29,
        41,
        17,
        39,
        53,
        23,
        57,
        66,
        25,
        67,
        31,
        50,
        47,
        50,
        20,
        33,
        48,
        64,
        51,
        62,
        44,
        33,
        45,
        52,
        60,
        39,
        26,
        47,
        59,
        55,
        19,
        38,
        42,
        59,
        63,
        35,
        45,
        61,
        61,
        69,
        41,
        67,
        40,
        29,
        68,
        36,
        47,
        68,
        56,
        36,
        41,
        ]

pss= [
    142,
    142,
    138,
    168,
    120,
    162,
    149,
    174,
    158,
    180,
    124,
    130,
    120,
    157,
    150,
    176,
    128,
    154,
    130,
    158,
    114,
    144,
    158,
    139,
    164,
    176,
    125,
    158,
    134,
    144,
    159,
    142,
    116,
    140,
    130,
    162,
    160,
    172,
    160,
    144,
    135,
    156,
    185,
    138,
    132,
    145,
    140,
    174,
    128,
    150,
    124,
    170,
    144,
    148,
    138,
    169,
    154,
    175,
    152,
    170,
    153,
    110,
    184,
    136,
    156,
    172,
    165,
    124,
    134,

]
x1MenosMediaDeX=[]
y1MenosMediaDeY=[]
multiplicacion=[]
potencia=[]
y=[]
residuos=[]
promX = statistics.mean(edades)
promY = statistics.mean(pss)
print('PROMEDIO DE X:')
print(promX)
print('PROMEDIO DE Y:')
print(promY)


a = 0
b = 68
for i in range(b+1):
    x1MenosMediaDeX.append(edades[a]-promX)
    a=a+1

c = 0
d = 68
print('-----------------------------------------------------------')
for i in range(d+1):
    y1MenosMediaDeY.append(pss[c]-promY)
    c=c+1

e = 0
f = 68
for i in range(f+1):
    multiplicacion.append(x1MenosMediaDeX[e]*y1MenosMediaDeY[e])
    e=e+1

g = 0
h = 68
for i in range(h+1):
    potencia.append(pow(x1MenosMediaDeX[g],2))
    g=g+1


listSum = sum(multiplicacion)
print('SUMATORIA DE MULTIPLICACIONES:')
print(listSum)

listSumTwo = sum(potencia)
print('SUMATORIA DE POTENCIAS:')
print(listSumTwo)

m=listSum/listSumTwo
print('M:')
print(m)

b=promY-(m*promX)
print('B:')
print(b)

j = 0
k = 68
for i in range(k+1):
    y.append((m*edades[j])+b)
    j=j+1

n = 0
o = 68
for i in range(o+1):
    residuos.append(pss[n]-y[n])
    n=n+1

st_dev = statistics.pstdev(residuos)
print('DESVIACIÓN:')
print(st_dev)

cor =np.corrcoef(edades, pss)
print(cor)


plt.scatter(edades, pss, color = 'red')
plt.plot(edades, y, color = 'blue')
plt.title('Relacion de edades y su pss')
plt.xlabel('Edades')
plt.ylabel('Pss')
plt.show()


    

  
