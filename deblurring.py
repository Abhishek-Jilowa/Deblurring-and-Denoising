from matplotlib import lines
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
''' First Deblurred and then Denoised'''
''' Reading  data from csv file'''
data = pd.read_csv(r'C:\Users\sujal\Desktop\data.csv',delimiter=',',encoding='utf8') 
h= np.array([1/16 , 4/16 , 6/16 , 4/16 , 1/16]) #declaring impulse response h[n] as an array
y1 = np.array(data.y) #recieved signal Y[n]
x1= np.array(data.x)  
y_w = [] # List for storing DTFT
Y_W=[] # List for Storing absolute values of DTFT

for k in range(0,193):
    summ = 0
    for n in range(0,193):
        a = math.cos((2*math.pi*k*n)/193)
        b = -math.sin((2*math.pi*k*n)/193)
        z = complex(a,b)
        summ = summ +  y1[n]*z
    y_w.append(summ)
    Y_W.append(abs(summ))

'''Computing DTFT of Impulse Response h[n] '''
h_w = []
for k in range(0,193):
    pi=[]
    for n in range(-2,3):
        a = math.cos((2*math.pi*k*n)/193)
        b = -math.sin((2*math.pi*k*n)/193)
        z = complex(a,b)
        pi.append(z)
    exp = np.array(pi)
    p = np.multiply(h,exp)
    h_w.append(np.sum(p))
H_W=[]# List for storing DTFT
x_w = [] # List for Storing absolute values of DTFT of h[n]
for i in range(0,193):
    if h_w[i].real<0.5:
        x_w.append(y_w[i]/0.5)
    else:
        x_w.append(y_w[i]/h_w[i])
X_W = []
for i in range(193):
    X_W.append(abs(x_w[i]))
for i in range(193):
    H_W.append(abs(h_w[i]))


OPP = [(2*math.pi*i)/193 for i in range(193)]   #x-axis for graph ploting
x_axis = np.array(OPP)


plt.plot(x_axis,np.array(H_W),label='DTFT of y1[n]')
plt.xlabel('Ω-Omega')
plt.ylabel('|Y(e^(jΩ))|')
plt.legend()
plt.show()


plt.plot(x_axis,np.array(X_W),label='DTFT of h[n]')
plt.xlabel('Ω-Omega')
plt.ylabel('|H(e^(jΩ))|')
plt.legend()
plt.show()


plt.figure(figsize=(13,10))
plt.plot(x_axis,np.array(Y_W),label='DTFT of x[n]')
plt.xlabel('Ω-Omega')
plt.ylabel('|X(e^(jΩ))|')
plt.legend()
plt.show()

f_output = []
for n in range(0,193):
    summ = 0
    for k in range(0,193):
        x = math.cos((2*math.pi*k*n)/193)
        y = math.sin((2*math.pi*k*n)/193)
        z = complex(x,y)
        summ = summ + x_w[k]*z
    f_output.append(summ/193)    
#print(f_output or deblured output)
for j in f_output:
    print(j)

#Denoising after debluring by local mean denoising method
f_output.append(f_output[len(f_output)-1])
f_output.append(f_output[len(f_output)-1])
x1_1 = f_output[0]
f_output.insert(0,x1_1)
f_output.insert(0,x1_1)

Denoised = []#array corresponding to denoised signal after debluring


for t in range(2,len(f_output)-2):  #Denoising
    s = (f_output[t-2]+f_output[t-1]+f_output[t]+f_output[t+1]+f_output[t+2])/5
    Denoised.append(s)
print("Final values\n")

Denoised2 = []  #array corresponding to denoised signal after debluring
Denoised2.append(Denoised[0])
Denoised2.append(Denoised[1])
Denoised2.append(Denoised[191])
Denoised2.append(Denoised[190])

for t in range(2,len(Denoised)-2):  #Denoising 2nd time
    s = (Denoised[t-2]+Denoised[t-1]+Denoised[t]+Denoised[t+1]+Denoised[t+2])/5
    Denoised2.append(s)
print("Final values\n")

l1 = []
for s in Denoised2:
    l1.append(s.real)

x_axis = [i for i in  range(0,193)]

plt.plot(np.array(x_axis),np.array(l1),label='final output signal x2[n]')
plt.xlabel('n')
plt.ylabel('x2[n]')
plt.legend()
plt.show()

#compares orignal signal with final signal after deblur and denoise
plt.plot(np.array(x_axis),x1,label='Original Signal x[n]')
plt.plot(np.array(x_axis),np.array(l1),label='Final output Signal x2[n]')
plt.legend()
plt.xlabel('time')
plt.ylabel('temperature')
plt.show()

#Mean Squared Error of Final output
Error=np.subtract(x1,l1)
M=0
for i in Error:
    M+=i*i
print("Mean Squared error is ",round(M/193,3))