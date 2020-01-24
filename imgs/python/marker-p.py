# plot a funky shape :]

import numpy as np
import matplotlib.patches as patches
from matplotlib import pyplot as plt


pi = np.pi
cos = np.cos
sin = np.sin

#---- define a function to plot data

def plot_data(ax):
    
    ax.set_aspect(1)
  
    #-- interface shape

    phi = np.linspace(0,2.*pi,40)

    x = (1+.1*sin(3*phi))*cos(phi-pi/4)
    y = (1+.1*sin(3*phi))*sin(phi-pi/4)    

    ax.plot(x,y,'o',color='C0')
    ax.plot(x,y,linestyle='--',color='C0', alpha=0.6)
    
    #-- plot grid

    xmax=1.6
    xtick = np.linspace(-xmax, xmax, 13)  # +1 corresponds to staggered grid
    ytick = np.linspace(-xmax, xmax, 13)
    
    ax.axes.get_xaxis().set_ticks(xtick)
    ax.axes.get_yaxis().set_ticks(ytick)
    
    ax.grid(True)
    
    ax.get_xaxis().set_tick_params(which='both', direction='in')
    ax.get_yaxis().set_tick_params(which='both', direction='in')
    
    #-- No labels, no ticks

    ax.xaxis.set_major_formatter( plt.NullFormatter())
    ax.yaxis.set_major_formatter( plt.NullFormatter())

    ax.tick_params(bottom='off', top='off', left='off', right='off')
    
    return ax


#---- Script

if __name__ == '__main__':

    #---> Create the figure

    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(5, 5)

    ax = plot_data(ax)

    #---> Output and save

    plt.savefig('../marker-points.pdf', bbox_inches='tight')
    plt.show()
