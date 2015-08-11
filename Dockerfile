FROM python

RUN pip install cchardet
RUN pip install lasio

ADD main.py /app/

ENTRYPOINT ["python", "/app/main.py"]
