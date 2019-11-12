FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

COPY requirements.txt /usr/src/obs/requirements.txt

RUN pip3 install --no-cache-dir -r /usr/src/obs/requirements.txt

COPY Oracle.py /usr/src/obs/Oracle.py
COPY OracleDB.py /usr/src/obs/OracleDB.py

CMD ["python3", "/usr/src/obs/Oracle.py"]