from matplotlib.lines import lineMarkers, lineStyles
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages



def main():
    rng = np.random.default_rng(seed=42)
    N = 10
    yerr = 0.5
    x = np.linspace(1,10,N)
    y = 8.-(x+rng.normal(scale=yerr, size=N))
    coef = np.polyfit(x,y,1)
    poly1d_fn = np.poly1d(coef) 

    plt.errorbar(x,y,yerr, fmt='bo')
    plt.plot(x,poly1d_fn(x), color="red",linestyle="dashed")
    
    # axis labels with units
    plt.xlabel('$x$ (cm)')
    plt.ylabel('$y$')
    plt.savefig('test.pdf')




if __name__ == "__main__":
    main()
