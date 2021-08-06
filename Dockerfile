FROM ubuntu:18.04

WORKDIR /code

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

COPY requirements.txt /code

COPY . /code

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD python3 src/tests.py && python3 src/app.py