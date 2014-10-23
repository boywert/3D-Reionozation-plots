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
    output.data = numpy.fromfile(f,numpy.float32,output.grid[0]**3).reshape(( output.grid[0], output.grid[1], output. grid[2]))
    padd = numpy.fromfile(f,numpy.int32,1)[0]
    return output

def get_space(data3d,x,y,z):
    a = data3d[0:100,0:100,0:5]
    b = numpy.zeros(shape=(100,100), dtype=numpy.float64)
    for i in range(len(a)):
        for j in range(len(a[i])):
            b[i,j] = numpy.sum(a[i,j], dtype=numpy.float64)/5
    return b

filename = "/mnt/lustre/scratch/cs390/codes/ionz_codes/withoutprevxfrac/38000.00/xfrac3d_8.064.bin"

xfrac = read_xfrac(filename)
print get_space(xfrac.data,10,20,10)

#mean = numpy.sum(xfrac.data,dtype=numpy.float64)/(xfrac.grid[0]*xfrac.grid[1]*xfrac.grid[2])
#xfrac.data = xfrac.data/mean - 1.0

#ps = numpy.absolute(numpy.fft.rfftn(xfrac.data))
#print ps
 
