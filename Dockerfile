FROM python

ENV ROW_SIZE 100000
ENV COL_SIZE 50

RUN pip install lasio
RUN pip install memory_profiler
RUN pip install psutil
RUN pip install pympler

ADD main.py /app/

ENTRYPOINT ["python", "/app/main.py"]
