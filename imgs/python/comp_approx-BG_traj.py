import sys
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

"""
An approximate ODE system for two equal spheres in shear.
See correspondance with Itzhak Fouxon (2018-08-06).
"""


params = {'text.usetex' : True,
          'font.size' : 11,
          'font.family' : 'lmodern',
          'text.latex.unicode' : True}

plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)

#---- System of ODEs

def system(var,t):

    a = 1. # radius
    x, z = var  # unpack variables

    r = np.sqrt(x**2+z**2)
    A = 5.*(a/r)**3 -8.*(a/r)**5 +25.*(a/r)**6 -35.*(a/r)**8
    B = 16/3.*(a/r)**5 -25/3.*(a/r)**8

    # list of RHS
    derivs = [(1-B/2.)*z -(A-B)*x**2*z/r**2,      
             -B/2.*x -(A-B)*x*z**2/r**2]

    return derivs


#---- Plotting

def plot_data(ax, x,z, N):

    ax.set_aspect(1)

    theta = np.linspace(0.,2.*np.pi,100)
    c0 = ax.plot(.95*np.cos(theta),.95*np.sin(theta),'--k')
    #c0 = ax.plot(10.*np.cos(theta),10.*np.sin(theta),'--k')

    for i in range(N):
        
        #c1 = ax.plot(x[i][0], z[i][0], 'o', color='C0') # initial state            
        c2 = ax.plot(x[i], z[i], color='k')

    ax.set_xlim(-8,8)
    ax.set_ylim(-4,4)

    #ax.set_xlabel(r'$x/a$')
    #ax.set_ylabel(r'$z/a$')
    
    ax.get_xaxis().set_tick_params(which='both', direction='in')
    ax.get_yaxis().set_tick_params(which='both', direction='in')

    #-- No labels, no ticks
    
    ax.xaxis.set_major_formatter( plt.NullFormatter())
    ax.yaxis.set_major_formatter( plt.NullFormatter())
    
    ax.tick_params(bottom='off', top='off', left='off', right='off')
    
    #ax.legend(['a','b'],frameon=False, loc=1)
    #ax.text(.03, .0005, r'$\propto \Delta x^2$')
    
    
    return ax


#---- Main script

if __name__  == '__main__':

    t = np.arange(0.,800.,2e-3) # time (start,end,step)

    # initial separation (in the unit of diameter)

    x0_all = np.arange(-8., -1., 1)
    z0 = 0.

    i = 0         # loop count
    x, z = [], [] # solution lists
    
    for x0 in x0_all:
        
        var0 = [x0, z0] # init. sep. packed for the ODE solver
        soln = odeint(system, var0, t) # the ODE solver
    
        x.append(soln[:,0])
        z.append(soln[:,1])
    
        i += 1

    # sweep in another direction
    
    x0 = -8.0
    z0_all = np.arange(0., 4, 0.6)
        
    for z0 in z0_all:
    
        #if z0 > 0.: x0 = -8.0 
        
        var0 = [x0, z0] # init. sep. packed for the ODE solver
        soln = odeint(system, var0, t) # the ODE solver
    
        x.append(soln[:,0])
        z.append(soln[:,1])
    
        i += 1

    # sweep in the thrid direction
    
    x0 = 8.0
    z0_all = np.arange(0., -4, -0.6)
        
    for z0 in z0_all:
    
        #if z0 > 0.: x0 = -8.0 
        
        var0 = [x0, z0] # init. sep. packed for the ODE solver
        soln = odeint(system, var0, t) # the ODE solver
    
        x.append(soln[:,0])
        z.append(soln[:,1])
    
        i += 1
        
    # Plot in a figure

    fig, ax = plt.subplots(1, 1, sharey=True)
    fig.set_size_inches(6,3)

    ax = plot_data(ax, x,z, i)

    ax.tick_params(axis='both', which='both', length=0)

    plt.savefig('../BG-traj4.pdf', bbox_inches='tight', transparent=False)
    plt.show()
