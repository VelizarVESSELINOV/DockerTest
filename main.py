"Test memory usage"
from os import environ
from os.path import getsize

from lasio import LASFile, read
from memory_profiler import profile
from numpy import arange, nanmax, nanmean, nanmin
from numpy.random import rand
from pympler.muppy import get_objects
from pympler.summary import get_diff, print_, summarize


@profile
def create_file(rows, cols):
    "Crete file"
    las = LASFile()
    las.add_curve("MDEPTH", arange(rows), unit="mm")

    for i in range(cols):
        las.add_curve("RND_{:02d}".format(i + 1), rand(rows), descr="Random")

    file_name = "file" + str(rows) + ".las"

    with open(file_name, "w") as file:
        las.write(file, version=2.0)

    del las
    return file_name


@profile
def file_test(rows=500000, cols=50):
    "File test"
    print("Creating file with {} rows and {} columns".format(rows, cols))
    file = create_file(rows, cols)
    print("Size of the file: {:.2f} MiB".format(getsize(file) / (1024 * 1024)))
    print("Reading file")
    sum1 = summarize(get_objects())
    las = read(file)
    sum2 = summarize(get_objects())
    diff = get_diff(sum1, sum2)
    print_(diff)

    for curve in las.curves:
        print("Name: {}, Min: {:.2f}, Mean: {:.2f}, Max: {:.2f}"
              .format(curve.mnemonic, nanmin(curve.data), nanmean(curve.data),
                      nanmax(curve.data)))

    del las
    las = read(file)
    del las
    las = read(file)
    del las
    las = read(file)
    del las
    print("Happy end")


def main():
    "Main function"
    try:
        cols = int(environ['COLUMN_SIZE'])
        rows = int(environ['ROW_SIZE'])
    except KeyError:
        file_test()
    else:
        file_test(rows, cols)

if __name__ == "__main__":
    main()
