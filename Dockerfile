FROM python:3.8-slim-buster

WORKDIR /code

RUN pip install pandas matplotlib

CMD ["python", "main.py"]
