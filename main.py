from lasio import LASFile, read, HeaderItem
from numpy import arange
from numpy.random import rand
from datetime import datetime as dt


def createFile(size):
    l = LASFile()
    depth = arange(size)
    data = rand(size)
    l.params["ENGI"] = HeaderItem("ENGI", "", "toto", "tata")
    l.add_curve("DEPT", depth, unit="mm")
    l.add_curve("RND", data, descr="Made-up curve data for example")
    fn = "file" + str(size) + ".las"

    with open(fn, "w") as f:
        l.write(f, version=2.0)

    return fn

size = 10000000
print("Creating file with {} rows".format(size))
f = createFile(size)
print("Reading file")
print(read(f))
print("Happy end")
