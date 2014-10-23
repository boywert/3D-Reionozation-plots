import numpy

class xfrac:
    grid = 0
    data = 0

def read_xfrac(filename):
    f = open(filename,"rb")
    output = xfrac()
    padd = numpy.fromfile(f,numpy.int32,1)[0]
    output.grid = numpy.fromfile(f,numpy.int32,3)
    padd = numpy.fromfile(f,numpy.int32,1)[0]
    padd = numpy.fromfile(f,numpy.int32,1)[0]
    output.data = numpy.fromfile(f,numpy.float32,output.grid[0]**3).reshape((grid[0],grid[1],grid[2]))
    padd = numpy.fromfile(f,numpy.int32,1)[0]
    return output

filename = "/mnt/lustre/scratch/cs390/47Mpc/couple/model_001/xfrac/5500.00/5500.00/xfrac3d_8.064.bin"

xfrac = read_xfrac(filename)
print numpy.sum(xfrac.data,dtype=numpy.float64)/(xfrac.grid[0]*xfrac.grid[1]*xfrac.grid[2])
