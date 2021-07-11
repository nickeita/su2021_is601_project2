FROM python:3.9

ADD src /src

ENV PYTHONPATH=src

CMD ["python", "./src/runTestProcess.py"]