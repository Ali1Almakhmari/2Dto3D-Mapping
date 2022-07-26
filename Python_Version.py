##
#By Ali Almakhmari, 07/02/2022
##
import numpy as np
from numpy import * 
import cv2 
import plotly.graph_objects as go
from numpy import flipud
from plotly.subplots import make_subplots

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
    
X,Y,Z = ellipsoid(0, 0, 0, a, a, b, 800)
image = cv2.imread(pictureName , cv2.COLOR_BGR2RGB)
image = np.flip(image, axis=-1) 
surfcolor = np.flipud(image)/255



fig=go.Figure(data=[go.Surface(x=X, y=Y, z=Z, surfacecolor=surfcolor)]) 
fig.update_layout(title='Color corresponds to distance to origin', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.show()
