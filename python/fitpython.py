#PROGRAMMA ANALISI DATI SUPREMO
import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.optimize
import scipy.stats
import os
import pylab

"""

#MEDIA DI TUTTE LE MISURE
y = []
erry=[]
numpunti=2

numdati= 3 #numero di misure fatte di un punto
for i in range(0,numpunti):
    dati = [] #inizializziamo il vettore dove mettiamo le misure
    for j in range(0,numdati):
        misura = float(input("Immettere misura acquisita: "))
        dati.insert(j,misura)
        print (dati)
    y.insert(i, scipy.mean(dati))    
    erry.insert(i, scipy.std(dati))
    print (y)
    print (erry)
    
#ABBIAMO CREATO IL VETTORE CON LE ORDINATE Y DEL NOSTRO GRAFICO


"""
#INPUT
x=[0.519,0.582,0.662,0.734,0.786]
y=[2.093,2.35,2.667,2.955,3.161]
erry=[0.0051,0.0048,0.0041,0.0034,0.0038] #errori solo su y
npoint=len(x) #numero di punti sperimentale

#MEDIA E VARIANZA

#ISTRUZIONI PER DISEGNARE
plt.xlim(0,1) #scelta del range in x della figura
plt.ylim(0,4) #scelta del range in y della figura


#CALCOLO DEL FIT 
Sx=0.
Sy=0.
Sxx=0.
Sxy=0.
Serr=0.
for i in range(0,npoint):
    Sx+=x[i]/erry[i]**2
    Sy+=y[i]/erry[i]**2
    Sxx+=x[i]*x[i]/erry[i]**2
    Sxy+=x[i]*y[i]/erry[i]**2
    Serr+=1/erry[i]**2
    
den=(Serr*Sxx-Sx**2)

a=Sy*Sxx-Sx*Sxy #calcolo del termine noto
a=a/den 
b=Serr*Sxy-Sx*Sy #calcolo della pendenza
b=b/den
erra=Sxx/den #calcolo errore termine noto
erra=np.sqrt(erra)
errb=Serr/den #calcolo errore su pendenza
errb=np.sqrt(errb)


#CALCOLO DEL CHI QUADRO
chi2=0
for i in range(0,npoint):
    tmp=y[i]-(b*x[i]+a)
    tmp=tmp/erry[i]
    tmp=tmp*tmp
    chi2+=tmp
print('chi2=%f\n ' % chi2 )
print(' a = %f +- %f\n' %(a,erra))
print(' b = %f +- %f\n' %(b,errb))

plt.errorbar(x,y,erry) #comando per disegnare i punti

z=np.linspace(0,6,100)
f=b*z+a
pylab.plot(z,f,color= 'red')


plt.show()  #disegna
