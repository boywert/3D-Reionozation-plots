import numpy
import pylab
from pylab import *
from matplotlib import gridspec

class xfrac:
    grid = 0
    data = 0

def read_xfrac(filename,doubleflag):
    f = open(filename,"rb")
    output = xfrac()
    padd = numpy.fromfile(f,numpy.int32,1)[0]
    output.grid = numpy.fromfile(f,numpy.int32,3)
    padd = numpy.fromfile(f,numpy.int32,1)[0]
    padd = numpy.fromfile(f,numpy.int32,1)[0]
    if(doubleflag == 1):
        output.data = numpy.fromfile(f,numpy.float64,output.grid[0]**3).reshape(( output.grid[0], output.grid[1], output. grid[2]))
    else:
        output.data = numpy.fromfile(f,numpy.float32,output.grid[0]**3).reshape(( output.grid[0], output.grid[1], output. grid[2]))
    padd = numpy.fromfile(f,numpy.int32,1)[0]
    return output

def get_space(data3d,x,y,z):
    minx = x[0]
    maxx = x[1]
    miny = y[0]
    maxy = y[1]
    minz = z[0]
    maxz = z[1]
    a = data3d[minx:maxx,miny:maxy,minz:maxz]
    b = numpy.zeros(shape=((maxx-minx),(maxy-miny)), dtype=numpy.float64)
    for i in range(len(a)):
        for j in range(len(a[i])):
            b[i,j] = numpy.sum(a[i,j], dtype=numpy.float64)/(maxz-minz)
    return b

def get_plot(filename,doubleflag,x,y,z):
    xfrac = read_xfrac(filename,doubleflag)
    data_plot = get_space(xfrac.data,x,y,z) 
    return data_plot

#global x,y,z


def plot_reionized(redshift):
    x = (0,306)
    y = (0,306)
    z = (200,205)
    fig = pylab.figure()
    gs = gridspec.GridSpec(1, 3, width_ratios=[1,1,1]) 
    ax6 = pylab.subplot(gs[0,0])
    filename = "/mnt/lustre/scratch/cs390/codes/ionz_codes/nosuppresswithhist/5500.00/xfrac3d_"+redshift+".bin"
    data_plot = get_plot(filename,0,x,y,z)
    im6= ax6.imshow(data_plot, cmap=cm.RdBu, vmin=0.0, vmax=1.0, extent=[x[0], x[1], y[0], y[1]])
    ax6.axis("off")
    #im6.set_interpolation('bilinear')

    ax4 = pylab.subplot(gs[0,1])
    filename = "/mnt/lustre/scratch/cs390/codes/ionz_codes/okamotowithhist/5500.00/xfrac3d_"+redshift+".bin"
    data_plot = get_plot(filename,0,x,y,z)
    im4 = ax4.imshow(data_plot, cmap=cm.RdBu, vmin=0.0, vmax=1.0, extent=[x[0], x[1], y[0], y[1]])
    ax4.axis("off")
    #im4.set_interpolation('bilinear')    
    ax5 = pylab.subplot(gs[0,2])
    filename = "/mnt/lustre/scratch/cs390/47Mpc/couple/model_001/xfrac/5500.00/xfrac3d_"+redshift+".bin"
    data_plot = get_plot(filename,0,x,y,z)
    im5 = ax5.imshow(data_plot, cmap=cm.RdBu, vmin=0.0, vmax=1.0, extent=[x[0], x[1], y[0], y[1]])
    ax5.axis("off")
    #im5.set_interpolation('bilinear')
    #cb = fig.colorbar(im1, ax=ax1 )
    fig.savefig(redshift+"_pic.pdf", bbox_inches='tight')
    
plot_reionized("9.938")
plot_reionized("9.457")
plot_reionized("9.026")
plot_reionized("8.515")
plot_reionized("7.960")
plot_reionized("7.480")
plot_reionized("6.981")
plot_reionized("6.483")

