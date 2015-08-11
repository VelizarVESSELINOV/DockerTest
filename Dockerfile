FROM python

ENV ROW_SIZE 10000000

RUN pip install lasio

ADD main.py /app/

ENTRYPOINT ["python", "/app/main.py"]
