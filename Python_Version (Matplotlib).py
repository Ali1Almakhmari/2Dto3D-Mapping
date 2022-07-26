import numpy as np
from numpy import * 
import cv2 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
# %matplotlib notebook
# %matplotlib widget
from IPython.display import Javascript
from numpy import flipud


#%matplotlib widget
from plotly.subplots import make_subplots

from matplotlib import cm

  
# importing required libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from matplotlib.ticker import LinearLocator


# %matplotlib inline
fig=plt.figure()
ax=plt.axes(projection="3d");
#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
def sphere(n):
    n2n = np.arange(-n,n+1,2)
    theta = (n2n/n*pi).reshape(1,len(n2n))
    phi = n2n / n*pi/2
    phi = phi.reshape(len(phi),1)
    cosphi = cos(phi); cosphi[0] = 0; cosphi[n] = 0;
    sintheta = sin(theta); sintheta[0,0] = 0; sintheta[0,n] = 0
    x = cosphi@cos(theta)
    y = cosphi@sintheta;
    z = sin(phi)@ones([1,n+1])
    return x,y,z


def ellipsoid(*varargin):
    xc,yc,zc,xr,yr,zr,n = varargin
    n  = 20
    if len(varargin) > 6:
        n = varargin[6]
    x,y,z = sphere(n)
    x = xr*x+xc;
    y = yr*y+yc;
    z = zr*z+zc;
    return x,y,z


pictureName = "mars.png" #the 2D picture's name of Mars: "mars.png"

R = 3397200 #Mars equatorial radius in meters
f = 1999/339619 #flatenning factor of Mars

a = R #semi-major axis in meters
b = (1-f)*a #semi-minor axis in meters
    
X,Y,Z = ellipsoid(0, 0, 0, a, a, b, 800) #increase the number of panels (800) to increase the accuracy of the ellispoid

image = cv2.imread(pictureName , cv2.COLOR_BGR2RGB)
image = np.flip(image, axis=-1) 
surfcolor = np.flipud(image)/255


# Plot the surface.
surf = ax.plot_surface(X, Y, Z, rstride=5,cstride=5,facecolors = surfcolor,
                       linewidth=0,color = 'red')

# Customize the z axis.
ax.zaxis.set_major_locator(LinearLocator(10))

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
