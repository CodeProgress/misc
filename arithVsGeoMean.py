import pylab

def avg(x,y):
    return (x+y)/2.
    
def geoMean(x, y):
    return (x*y)**.5

def plot_arith_geo(lower = 1, upper = 10, showDiff = False):

    pylab.plot([avg(x, y) for x in range(lower,upper) for y in range(x)],
                label = "Arithmetic Mean")
    
    pylab.plot([geoMean(x,y) for x in range(lower,upper) for y in range(x)],
                label = "Geometric Mean")
    
    if showDiff:            
        pylab.plot([avg(x,y)-geoMean(x,y) for x in range(lower,upper) for y in range(x)],
                    label = "ArithMean - GeoMean")
    
    pylab.legend(loc = 2)
    pylab.show()


def plot_arith_geo_scatter(lower = 1, upper = 10):
    pylab.scatter([avg(x, y) for x in range(lower,upper) for y in range(x)],
                [geoMean(x,y) for x in range(lower,upper) for y in range(x)],
                label = "For cominations of (a,b) {} <= a < b < {}".format(str(lower), str(upper)))
    
    pylab.plot([x for x in range(10)], label = "Line x = y")
    
    pylab.xlabel("Arithmetic Mean")
    pylab.ylabel("Geometric Mean")
    
    pylab.legend(loc = 2)
    
    pylab.show()

plot_arith_geo()
#plot_arith_geo_scatter()

