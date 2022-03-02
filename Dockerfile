# Dockerfile
FROM python:3.7
COPY requirements.txt /flask-example/requirements.txt
WORKDIR /orderapp
RUN pip install -r requirements.txt
COPY . /flask-example
ENTRYPOINT ["python"]
CMD ["app.py"]