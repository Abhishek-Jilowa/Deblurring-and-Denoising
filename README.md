# Deblurring-and-Denoising
Description:
One of the many applications of Internet of Things (IoT) consists of continuous monitoring of temperature in an area. To that end, several temperature sensors are installed at different locations. These sensors measure 
and store the recorded value of temperature over time. However, due to limitations of hardware, the sensor memory needs to be cleared periodically and this is done by transmitting the stored values to a base unit. Assume that x[n] denotes the samples of the true value of temperature recorded by a sensor. However, it is found that the received signal y[n] at the base unit suffers from blur distortions and noise (additive). Hence, the signal y[n] needs to be first processed so that we can recover x[n] from it. Assume that blur happens via a system characterized an impulse response h[n] = 1/16[1 4 6 4 1] (assume that the center value of 6/16 corresponds to n = 0). Then, implement the following two approaches to recover the original signal x[n] from distorted signal y[n].
1. First remove noise and then sharpen (deblur). Let the resulting signal be x1[n].
2. First sharpen (deblur) and then remove noise. Let the resulting signal be x2[n].

Steps:
To run the code and following the given instruction:
1) Open the .py file codes in VScode editor.
2) Install python3.9.0 and follwing libraries on your system
 numpy 
 math
 matplotlib.pyplot
 pandas

3)Now place your csv file location in place of Data.csv in given code.
4)Now run the codes , the code will show graphs of x1(n) and x2(n) respectively.
5) At last, the code will print 2 values of MSE and the lesser MSE is more efficient.
