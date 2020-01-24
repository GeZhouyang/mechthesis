# plot a funky shape :]

import numpy as np
import matplotlib.patches as patches
from matplotlib import pyplot as plt

params = {'text.usetex' : True,
          'font.size' : 12.5,
          'font.family' : 'lmodern',
          'text.latex.unicode' : True}

plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)
plt.rc('axes', labelsize=16)


pi = np.pi
cos = np.cos
sin = np.sin

#---- define a function to plot data

def plot_data(ax, x,y):
      
    ax.plot(x,y,'o', mec='k', mfc="None")
    ax.plot(x,y,'k')

    # plot droplet
    ax.plot([center-radius,center-radius],[-2,2], '--', color='C7', alpha=0.5)
    ax.plot([center+radius,center+radius],[-2,2], '--', color='C7', alpha=0.5)

    ax.set_xlim(xmin,xmax)
    
    #ax.get_xaxis().set_tick_params(which='both', direction='in')
    #ax.get_yaxis().set_tick_params(which='both', direction='in')
    #
    ##-- No labels, no ticks
    #
    #ax.xaxis.set_major_formatter( plt.NullFormatter())
    #ax.yaxis.set_major_formatter( plt.NullFormatter())
    #
    #ax.tick_params(bottom='off', top='off', left='off', right='off')
    
    return ax


#---- Script

if __name__ == '__main__':

    # grid
    xmin = 0
    xmax = 2
    dx = 1/10
    dxh = dx/2
    N = 20
    x = np.linspace(xmin+dxh, xmax-dxh, N)

    # 1D droplet
    center = 1+dx/3
    radius = 0.5
    
    # level set
    phi = abs(x-center)- radius

    # volume-of-fluid
    vof = []
    for xx,pp in enumerate(phi):
        if pp > dxh:
            vof.append(0)
        elif pp < -dxh:
            vof.append(1)
        else:
            vof.append( (dxh-pp)/dx )

    # phase field
    epsilon = 1*dx  # interface thickness
    pf = 0.5*( 1. + np.tanh(-phi/epsilon) )
            
    #---> Create the figure

    fig, ax = plt.subplots(3, 1, sharex=True)
    fig.set_size_inches(7,5)
    
    ax[0] = plot_data(ax[0], x,vof)
    ax[0].set_ylabel(r'$C$')
    ax[0].set_ylim(ymin=-0.06,ymax=1.06)
    
    ax[1] = plot_data(ax[1], x,phi)
    ax[1].set_ylabel(r'$\phi$')
    ax[1].set_ylim(ymin=-0.5,ymax=0.5)
    
    ax[2] = plot_data(ax[2], x,pf)
    ax[2].set_xlabel(r'$x$')
    ax[2].set_ylabel(r'$c$')
    ax[2].set_ylim(ymin=-0.06,ymax=1.06)
    
    #---> Output and save

    plt.savefig('../front-capture-comp.pdf', bbox_inches='tight')
    plt.show()
