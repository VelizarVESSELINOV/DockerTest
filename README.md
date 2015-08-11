# DockerTest

```
docker build -t velizar/test1 DockerTest
docker run -e ROW_SIZE=1000000 -t velizar/test1
docker run -e ROW_SIZE=10000000 -t velizar/test1
```

```
bash-3.2$ docker run -e ROW_SIZE=1000000 -t velizar/test1
Creating file with 10000000 rows
Reading file
bash-3.2$ docker run -e ROW_SIZE=10000000 -t velizar/test1
Creating file with 10000000 rows
Reading file
bash-3.2$
```
