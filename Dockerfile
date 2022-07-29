FROM python:3.8

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN python udp_server.py               

COPY . /app
EXPOSE 8001