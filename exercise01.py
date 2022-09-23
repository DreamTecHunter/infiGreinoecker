# exercise01
import numpy
from matplotlib import pyplot
from scipy import stats

# 1.1.1
myArangeData00 = numpy.arange(100, 200, 1)

# 1.1.2
myArangeData01 = numpy.arange(100, 200, 2)

# 1.1.3
myArangeData02 = numpy.arange(100, 100, 0.1)

# 1.1.4
myNormData00 = numpy.random.normal(0, 1, 100)
myUniData00 = numpy.random.uniform(0, 200, 1000000)

# 2.1

myNormData00Average = myNormData00.mean()
print(myNormData00Average)