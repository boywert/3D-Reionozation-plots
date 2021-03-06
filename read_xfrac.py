import numpy
import pylab
from pylab import *
from matplotlib import gridspec

class xfrac():
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
        output.data = numpy.fromfile(f,numpy.float64,output.grid[0]**3)
    else:
        output.data = numpy.fromfile(f,numpy.float32,output.grid[0]**3)
    xfr = numpy.sum(output.data, dtype=numpy.float64)/output.grid[0]**3
    return xfr

zlistfile = "/mnt/lustre/scratch/cs390/47Mpc/snap_z3.txt"
zlist_str = open(zlistfile,"r").readlines()
z = []
for i in range(len(zlist_str)):
    zlist_str[i] = zlist_str[i].strip()
    z.append(float(zlist_str[i]))

model_names = ["no_suppress","okamoto","patchy_I"]
filelist = ["/mnt/lustre/scratch/cs390/codes/ionz_codes/nosupwithnohist/43000.00/","/mnt/lustre/scratch/cs390/codes/ionz_codes/okamotowithnohist/43000.01/","/mnt/lustre/scratch/cs390/47Mpc/couple/model_002/xfrac/43000.00/"]
doubleflaglist =[0,0,0]

xf = {}
for i in range(len(model_names)):
    index = model_names[i]
    xf[index] = []
    for j in range(len(z)):
        filename = filelist[i]+"/xfrac3d_"+zlist_str[j]+".bin"
        xfd =  read_xfrac(filename,0)
        xf[index].append(xfd)

for i in range(len(z)):
    print z[i],xf[model_names[0]][i],xf[model_names[1]][i],xf[model_names[2]][i]
