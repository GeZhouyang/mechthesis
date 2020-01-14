# Illustrating mass-correction

import sys
import numpy as np
import matplotlib.patches as patches
from matplotlib import pyplot as plt

params = {'text.usetex' : True,
          'font.size' : 11,
          'font.family' : 'lmodern',
          'text.latex.unicode' : True}

plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)
colors = ['k','b','r','g'] # specify colors consistently


#---- define a function to plot data

def plot_data(ax, x,y, u,v, label):

    #-- dimensions & size
    xpc,ypc = 0,0 
    
    ax.set_aspect(1)

    ws = 1.5  # add some white space
    xmin1 = xmin -ws
    xmax1 = xmax +ws

    ax.set_xlim(xmin1, xmax1)
    ax.set_ylim(xmin1, xmax1)
  
    ##-- draw lines
    #ax.plot([xmin1,xmax1],[0,0],'--k', alpha=0.2)
    #ax.plot([0,0],[xmin1,xmax1],'--k', alpha=0.2)
    
    #-- cover sphere inside    
    c1 = plt.Circle((xpc,ypc), radius=0.3, color='r')
    ax.add_patch(c1)
    
    #-- draw arrows & add texts
    if label == 'stokes':
        ax.arrow(0,0, 1,0, width=0.15, color='r')
        ax.text(2.,-0.5, 'F', color='r', fontsize=16)
    elif label == 'stress':
        ax.arrow(-2,0, 1,0, width=0.15, color='r')
        ax.arrow( 2,0,-1,0, width=0.15, color='r')
        ax.text(-.45,-1.7, 'F', color='r', fontsize=16)

    #-- velocity

    s = 1 # step
    dxh=0.

    # direction
    vel = np.sqrt(np.add(np.square(u),np.square(v)))
    #u0 = np.divide(u,vel)
    #v0 = np.divide(v,vel)
    """ The following two lines are more robust """
    u0 = np.divide(u,vel, out=np.zeros_like(u), where=abs(vel)>1e-9)
    v0 = np.divide(v,vel, out=np.zeros_like(v), where=abs(vel)>1e-9)
    
    q0 = ax.quiver(x[::s,::s],y[::s,::s], u0[::s,::s],v0[::s,::s],
                   scale=15., width=0.0075, pivot='mid',
                   color=['#A9A9A9'], edgecolors=['#A9A9A9'])  # darkgray
    # magnitude
    q1 = ax.quiver(x[::s,::s],y[::s,::s], u[::s,::s],v[::s,::s],
                   scale=20, width=0.012,  pivot='mid',
                   color=colors[0], edgecolors=colors[0])

    #-- No labels, no ticks
    
    ax.xaxis.set_major_formatter( plt.NullFormatter())
    ax.yaxis.set_major_formatter( plt.NullFormatter())
    
    ax.tick_params(bottom='off', top='off', left='off', right='off')
    
    
    return ax


#---- Script

if __name__ == '__main__':

    #---> Parameters

    #let = 'stokes'
    let = 'stress'

    xmin,xmax = -10.,10.  # distance should be >> 1
    
    itot = 10 # should be an even number to avoid division by zero
    
    x = np.linspace(xmin,xmax,itot)
    y = np.linspace(xmin,xmax,itot)

    x1d, y1d = [],[]
    u1d_stokes, v1d_stokes = [],[]
    u1d_stress, v1d_stress = [],[]  

    #---> Data
    
    for i,xx in enumerate(x):
        for j,yy in enumerate(x):

            x1d.append(xx)
            y1d.append(yy)

            r  = np.sqrt(xx**2 + yy**2)
            r3 = r**3
            r5 = r**5
            buf= xx**2 - yy**2

            # Stokeslet flow
            u1d_stokes.append(1/r+xx**2/r3)
            v1d_stokes.append(xx*yy/r3)

            # Stresslet flow
            u1d_stress.append(-xx*buf/r5)
            v1d_stress.append(-yy*buf/r5)
            
    # generate the grid ...
    x2d = np.reshape(x1d,(itot,itot))
    y2d = np.reshape(y1d,(itot,itot))
    
    # ... and the velocity fields
    u2d_stokes = np.reshape(u1d_stokes,(itot,itot))
    v2d_stokes = np.reshape(v1d_stokes,(itot,itot))
    u2d_stress = np.reshape(u1d_stress,(itot,itot))
    v2d_stress = np.reshape(v1d_stress,(itot,itot))

    #---> Figure
    
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(4,4)

    if let == 'stokes':
        ax = plot_data(ax, x2d,y2d, u2d_stokes,v2d_stokes, let)
    elif let == 'stress':
        ax = plot_data(ax, x2d,y2d, u2d_stress,v2d_stress, let)

    ax.tick_params(axis='both', which='both', length=0)
    
    #---> Output and save
    
    plt.savefig('../'+let+'let1.pdf', bbox_inches='tight')
    plt.show()


    
