import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats
from scipy import constants as const


def loadCSV(name,hlines=1,split=2): #liest eine , getrennte CSV ein und teilt in arrays nach spalten
    hlines, data = ppk.readCSV(name,hlines)
    data = np.array(data)
    a,b=np.split(data,split)
    a = a[0] # anpassen nach split
    b = b[0]
    return a,b;

def plot(data):  # alle zeilen zum ploten von daten
    plt.plot(data[0],data[1],label="test")
    plt.legend()
    plt.title("Aufgabe 1 Baltt 3")
    plt.xlabel("Wellenzahl in 1/cm")
    plt.ylabel("Optische Dichte")
    plt.grid(True)
    plt.show()
    return;



def minmaxfind(a):
    #findet hoch und tiefpunkte, geht davon aus das zuerst ein Hochpunkt kommt
    #kann mit HP /TP im ersten bzw letzten wert nicht richtig umgehen
    HP = np.array([])
    TP = np.array([])
    l = len(a)
    j = a[0]
    HPisNext = 1
    for k in np.arange(1,l):
        i=a[k]
        if HPisNext == 1:
            if j>i:
                HP = np.hstack((HP,k-1))
                HPisNext=0
        elif HPisNext == 0:
            if j<i:
                TP = np.hstack((TP,k-1))
                HPisNext=1
        j=a[k]
    HP=np.int_(HP)
    TP=np.int_(TP)
    return HP,TP;



def main():
    hlines,data = ppk.readCSV("data_b3_a1.sec", 0)
    #plot(data)
    HP, TP = minmaxfind(data[1])
    #clean data
    HPdel = np.array([])
    for i in np.arange(len(HP)):
        if ( data[1][HP[i]] ) <= 0.05:
            HPdel = np.hstack((HPdel,i))

    HP = np.delete(HP,HPdel)
    HP = np.hstack((1,HP))

    #clean false postives
    HPdel = np.array([])
    for i in np.arange(len(HP)):
        if ( i%2 ) == 0:
            HPdel = np.hstack((HPdel,i))

    HP = np.delete(HP,HPdel)

    #Aufgabe a:
    print("Aufgabe 1a:")
    #plot incl j0->j1 und Text
    Q_i = 10 #index letztes P element
    j0 = 0
    j1 = 1
    for i in np.arange(len(HP)):
        if i == 0:     print("P-Zweig:");
        if i == Q_i+1: print("R-Zweig:");
        if i <= 10:
            j0 = (Q_i - i) + 1
            j1 = j0 - 1
            print("%2d w: %4.3f || j_0 = %02d -> j_1 = %02d" % (i, data[0][HP[i]], j0, j1 )  )
        else:
            j0 = (i - (Q_i+1))
            j1 = j0 + 1
            print("%2d w: %4.3f || j_0 = %02d -> j_1 = %02d" % (i, data[0][HP[i]], j0, j1 )  )



    plt.plot(data[0],data[1],label="Original Data")
    plt.plot(data[0][HP[:11]], data[1][HP[:11]], "gx", label = "P - Zweig Peaks")
    plt.plot(data[0][HP[11:]], data[1][HP[11:]], "rx", label = "R - Zweig Peaks")

    plt.legend()
    plt.title("Blatt 3: Aufgabe 1a")
    plt.xlabel("Wellenzahl in 1/cm")
    plt.ylabel("Optische Dichte")
    plt.grid(True)
    plt.show()
    plt.clf()

    #Aufgabe b:
    print("\n\nAufgabe 1b:")
    #Dwj0 = 2*B1* (2*j0 +1)
    #Dwj1 = 2*B0* (2*j1 +1)
    Dwj0 = np.array([])
    Dwj1 = np.array([])

    for i in np.arange(0,Q_i+1):
        #start with j0 = 1
        if i <= Q_i - 1:
            j0P = (Q_i - i)
            j0R = (Q_i + i + 2)
            dw = data[0][HP[j0R]] - data[0][HP[j0P]]
            Dwj0 = np.hstack((Dwj0, dw))
            print("%2d j_0 = %02d || \u0394w = %3.3f" % (i, i+1, dw))

        if i <= Q_i - 1:
            #start with j1 = 1
            j1P = Q_i -i -1
            j1R = Q_i +1 +i
            dw = data[0][HP[j1R]] - data[0][HP[j1P]]
            Dwj1 = np.hstack((Dwj1, dw))
            print("%2d j_1 = %02d || \u0394w = %3.3f" % (i, i+1, dw))

    #Aufgabe c:
    x_vals = 2 * ( np.arange(1,11) ) + 1
    x_s = np.linspace(0,25, 250)
    m0, c0, r_value, p_value, std_err = stats.linregress(x_vals, Dwj1)
    m1, c1, r_value, p_value, std_err = stats.linregress(x_vals, Dwj0)
    print("B_0 = %.4f  ||  B_1 = %.4f" % (m0/2, m1/2))

    plt.plot(x_vals, Dwj1, "bx", label = "Punkte zu B_0")
    plt.plot(x_vals, Dwj0, "gx", label = "Punkte zu B_1")
    plt.plot(x_s, m0*x_s+c0, "r-", label = "linreg: m = 2*B0")
    plt.plot(x_s, m1*x_s+c1, "r-", label = "linreg: m = 2*B1")

    plt.legend()
    plt.title("Blatt 3: Aufgabe 1c")
    plt.xlabel("j_0 ; j_1")
    plt.ylabel("\u0394\u03c9")
    plt.grid(True)
    plt.show()
    plt.clf()



    return;

main()
