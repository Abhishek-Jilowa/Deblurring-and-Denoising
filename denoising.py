from matplotlib import lines
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

'''first Denoise then Deblur'''
'''reading data from csv file'''
data = pd.read_csv(r'C:\Users\sujal\Desktop\data.csv',delimiter=',',encoding='utf8')  

h = np.array([1/16 , 4/16 , 6/16 , 4/16 , 1/16]) #impulse response as an array h

x1=data['x'].tolist()    #True signal
y1 = data['y'].tolist()  #signal recieved

#Denoising by local mean denoising method
y1.append(y1[len(y1)-1])
x11 = y1[0]
y1.insert(0,x11)

Y = []  #Y is array corresponding to denoised signal
Y.append(y1[0])
Y.append(y1[192])
for t in range(2,len(y1)-2):    #Denoising of signal
    sumi = (y1[t]+y1[t-1]+y1[t+1]+y1[t+2]+y1[t-2])/5
    Y.append(sumi)
print("Final values\n")
Y1=[]
Y1.append(Y[0])
Y1.append(Y[192])
Y1.append(Y[1])
Y1.append(Y[191])
for t in range(2,len(Y)-2):    #Denoising of signal
    sumi = (Y[t]+Y[t-1]+Y[t+1]+Y[t-2]+Y[t+2])/5
    Y1.append(sumi)
print("Final values\n")

for s in Y1:
    print(s)

"""Deblurring of denoised signal
   computing DTFT of Denoised signal"""
y_w = [] #list for storing computed DTFT 
Y_W=[]    #list for absolute value of computed DTFT
for k in range(0,193):
    summ = 0
    for n in range(0,193):
        summ = 0
    for n in range(0,193):
        x = math.cos((2*math.pi*k*n)/193)
        y = -math.sin((2*math.pi*k*n)/193)
        z = complex(x,y)
        summ = summ +  Y1[n]*z
    y_w.append(summ)
    Y_W.append(abs(summ))

#computing DTFT of h[n](impulse response)
h_w = []   #list for storing DTFT of h[n]
for k in range(0,193):
    pi=[]
    for n in range(-2,3):
        x = math.cos((2*math.pi*k*n)/193)
        y = -math.sin((2*math.pi*k*n)/193)
        z = complex(x,y)
        pi.append(z)
    expon = np.array(pi)
    PO = np.multiply(h,expon)
    h_w.append(np.sum(PO))
H_W=[]   #list for storing absolute value of DTFT of h[n]
xw = []
for i in range(0,193):
    if h_w[i].real<0.7:
        xw.append(y_w[i]/0.7)
    else:
        xw.append(y_w[i]/h_w[i])
X_W = []
for i in range(193):
    X_W.append(abs(xw[i]))
for i in range(193):
    H_W.append(abs(h_w[i]))

OPP = [(2*math.pi*i)/193 for i in range(193)]  #x-axis which will be used in graphs
x_axis = np.array(OPP)


plt.plot(x_axis,np.array(H_W),label='DTFT Of h[n]') #DTFT of h[n]
plt.xlabel('Ω-Omega')
plt.ylabel('|H(e^jΩ)|')
plt.legend()
plt.show()


plt.plot(x_axis,np.array(X_W),label='DTFT Of x[n]')  #DTFT of x[n]
plt.xlabel('Ω-Omega')
plt.ylabel('|X(e^jΩ)|')
plt.legend()
plt.show()


plt.figure(figsize=(13,10))  #DTFT of y[n]
plt.plot(x_axis,np.array(Y_W),label='DTFT Of Y[n]')
plt.xlabel('Ω-Omega')
plt.ylabel('|Y(e^jΩ)|')
plt.legend()
plt.show()

f_output = []
for n in range(0,193):
    summ = 0
    for k in range(0,193):
        x = math.cos((2*math.pi*k*n)/193)
        y = math.sin((2*math.pi*k*n)/193)
        z = complex(x,y)
        summ = summ + xw[k]*z
    f_output.append(summ/193)

    
#print(finaloutput)
for j in f_output:
    print(j)

plt.plot(x_axis,np.array(f_output),label='Recovered signal x1[n]')
plt.xlabel('time')
plt.xlabel('temprature')
plt.legend()
plt.show()

#compares orignal signal with final signal after deblur and denoise
plt.plot(x_axis,np.array(f_output),label='Recovered Signal x1[n]')  #comparing output signal with original signal
plt.plot(x_axis,np.array(x1),label='Orignal Signal x[n]')
plt.xlabel('time')
plt.ylabel('temperature')
plt.legend()
plt.show()

#Mean Squared Error
Error=np.subtract(x1,f_output)
M=0
for i in Error:
    M+=i*i
print("Mean Squared Error is ",round(M/193,3))