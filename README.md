# DockerTest

```
docker build -t velizar/test1 DockerTest
docker run -e ROW_SIZE=500000 -e COLUMN_SIZE=50 -t velizar/test1
docker run -e ROW_SIZE=10000000 -e COLUMN_SIZE=100 -t velizar/test1

# remove all the containers
docker rm `docker ps -qa`
```

```
bash-3.2$ docker run -e ROW_SIZE=100000 -e COLUMN_SIZE=50 -t velizar/test1
Creating file with 100000 rows and 50 columns
Size of the file: 53.60 MiB
Reading file
Name: MDEPTH, Min: 0.00, Mean: 49999.50, Max: 99999.00
Name: RND_01, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_02, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_03, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_04, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_05, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_06, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_07, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_08, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_09, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_10, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_11, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_12, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_13, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_14, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_15, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_16, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_17, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_18, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_19, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_20, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_21, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_22, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_23, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_24, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_25, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_26, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_27, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_28, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_29, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_30, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_31, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_32, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_33, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_34, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_35, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_36, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_37, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_38, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_39, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_40, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_41, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_42, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_43, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_44, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_45, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_46, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_47, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_48, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_49, Min: 0.00, Mean: 0.50, Max: 1.00
Name: RND_50, Min: 0.00, Mean: 0.50, Max: 1.00
Happy end
bash-3.2$ docker run -e ROW_SIZE=500000 -e COLUMN_SIZE=50 -t velizar/test1
Creating file with 500000 rows and 50 columns
Size of the file: 267.98 MiB
Reading file
bash-3.2$ echo $?
137
bash-3.2$ pip3 install memory_profiler
bash-3.2$ pip3 install psutil
bash-3.2$ python3 -m memory_profiler DockerTest/main.py

Filename: DockerTest/main.py

Line #    Mem usage    Increment   Line Contents
================================================
    29     20.2 MiB      0.0 MiB   @profile
    30                             def file_test(rows=500000, cols=50):
    31                                 "File test"
    32     20.2 MiB      0.0 MiB       print("Creating file with {} rows and {} columns".format(rows, cols))
    33     63.7 MiB     43.5 MiB       file = create_file(rows, cols)
    34     63.8 MiB      0.0 MiB       print("Size of the file: {:.2f} MiB".format(getsize(file) / (1024 * 1024)))
    35     63.8 MiB      0.0 MiB       print("Reading file")
    36    534.3 MiB    470.6 MiB       las = read(file)
    37
    38    538.6 MiB      4.3 MiB       for curve in las.curves:
    39    538.6 MiB      0.0 MiB           print("Name: {}, Min: {:.2f}, Mean: {:.2f}, Max: {:.2f}"
    40    538.6 MiB      0.0 MiB                 .format(curve.mnemonic, nanmin(curve.data), nanmean(curve.data),
    41    538.6 MiB      0.0 MiB                         nanmax(curve.data)))
    42
    43    273.2 MiB   -265.4 MiB       del las
    44    273.2 MiB      0.0 MiB       print("Happy end")
```
