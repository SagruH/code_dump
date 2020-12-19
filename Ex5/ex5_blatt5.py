import numpy as np
import PhyPraKit as ppk #wurde von mir verändert
import matplotlib.pyplot as plt

from scipy import stats
from scipy import constants as const
from scipy import signal

import itertools as it


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

def tetra(th, h, k, l ):
    lam = 1.54056
    a = 4.594
    c = 2.959

    LHS = (4 * (a**2) * np.sin(th)**2) / ( lam**2 )
    RHS = h**2 + k**2 + ( (a/c)**2 * l**2 )

    if np.abs(LHS-RHS) < 0.5:
        return True;
    else:
        return False;


def main():
    [th, I] = np.loadtxt("data_b7_a2.txt", unpack = True)

    #In = np.delete(I, (I!=0) )
    #thn = np.delete(th, (th!=0) )
    peaks, _ = signal.find_peaks(I, height = 1)
    HP, TP = minmaxfind(I)

    thw = th[peaks]

    #aufgabe 2
    ind = np.arange(0, 8)
    hk = it.combinations_with_replacement(ind,2)
    hkl = it.product(list(hk), ind)
    hkl = np.array(list(hkl))

    #reshape
    hkln = np.array([])
    for i in np.arange(len(hkl)):
        x = np.array([ hkl[i][0][0], hkl[i][0][1], hkl[i][1] ])
        hkln = np.hstack((hkln, x))
    hkl = hkln
    hkl = np.reshape(hkl, (-1, 3 ))

    #calculate
    sol = np.array([])
    for t, i in it.product(thw, hkl):
        if tetra(t, i[0], i[1], i[2]):
            sol = np.hstack((sol,[t,i]))


    j  = 0
    for i in np.arange(0,len(sol)-1, 2):
        print(j,": Theta:  ", sol[i], "  hkl:  ", sol[i+1])
        j += 1


    plt.plot(th[HP],I[HP],"xr")
    plt.plot(th,I, ".y")
    plt.plot(th,I, "-b")
    plt.grid(True)
    plt.show()
    return;

main()
