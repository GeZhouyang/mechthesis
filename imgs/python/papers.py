import numpy as np
import matplotlib.patches as patches
import pylab as pl
import matplotlib.colorbar as cbar
from matplotlib import pyplot as plt

params = {'text.usetex' : True,
          'font.size' : 11,
          'font.family' : 'lmodern',
          'text.latex.unicode' : True}

plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)


"""
Paper 1: ICLS/GFM
Paper 2: Soft-Matter
Paper 3: Itzhak 1
Paper 4: Itzhak 2
Paper 5: Marco
Paper 6: Hanna
Paper 7: DEM
"""

#---- define a function to plot data

def plot_data(ax):
      
    #-- rectangle lower left corner positions

    h = 0.7  # height of the rectangles
    Y = np.arange(1-h/2,7+h/2,1)  # y-coord
    X = [1,   2,  1, 2, 4,   0.6, 200]  # x-coord
    W = [200, 14, 3, 2, 564, 1.4, 1e4]  # width (+1) of the rectangles

    vs = [0, -.5, 0.7, 0.8, 0.2, -0.3, 0.4]  # [experimental --> theoretical] in [-1,1]
    normal = pl.Normalize(-1,1)
    colors = pl.cm.jet(normal(vs))

    X_txt = [5, 18, 4, 4, 7, 1.3, 800]
    txt = ['ICLS/GFM', 'droplet assembly',
           'hydrodynamic interaction I',
           'hydrodynamic interaction II',
           'droplets in turbulence',
           'liquid-infused surfaces','DLCD']

    for i,y in enumerate(Y): 
        rect = patches.Rectangle( (X[i],y), W[i]-1,h, color=colors[i])
        ax.add_patch(rect)
        ax.text(X_txt[i],y+0.2, txt[i])

    cax, _ = cbar.make_axes(ax) 
    cb2 = cbar.ColorbarBase(cax, cmap=pl.cm.jet,norm=normal)

    ax.plot([1,1],[0,8], linestyle='--',color='C7', alpha=0.5)
    
    #-- plot limit
    
    xmin = 0.5
    xmax = 1.5e4
    ymin = 0.4
    ymax = 7.6
    
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    
    ax.set_xscale('log')
    
    ax.set_xlabel(r'$N$')
    ax.set_ylabel(r'Paper')
    
    return ax


#---- Script

if __name__ == '__main__':

    #---> Create the figure

    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(6, 3.5)

    ax = plot_data(ax)

    #---> Output and save

    plt.savefig('../paper-diagram.pdf', bbox_inches='tight')
    plt.show()
