import numpy as np
import cmath
import matplotlib.pyplot as plt



def r_func(w):
    eb = 2.25
    wl = 50.876e12
    wt = 31.416e12
    
    eps = (eb * (wl**2 - w**2)/(wt**2 - w**2)) + 0J
    n = np.sqrt(eps)
    R = ( (n.real-1)**2 + n.imag ) / ( (n.real + 1)**2 + n.imag )
    
    return R;

def main():
    w = np.linspace(0,2e14,10000)
    wl = 50.876e12
    wt = 31.416e12
    
    plt.figure(figsize=(9, 7))
    plt.rcParams.update({'font.size': 16})
    plt.plot(w,r_func(w), label = "R")
    plt.vlines(wl, 0, 1.2, colors="r", linestyle = "dashed", label = "w_L")
    plt.vlines(wt, 0, 1.2, colors="g", linestyle = "dashed", label = "w_T")
    
    
    plt.legend()
    plt.title("Blatt 8 Aufgabe 3b")
    plt.xlabel("w in 1/s")
    plt.ylabel("R")
    plt.grid(True)
    plt.show()
    return;

main()


"""
Mit $n = \sqrt{\epsilon(\omega)}$ sowie:

$$
R = \frac{(\Re(n)-1)^2 + \Im(n)}{(\Re(n)+1)^2 + \Im(n)}
$$

Ergibt sich dieser Plot.
"""