FROM alpine:3.9.2

# install system dependencies
RUN apk update && apk add python3 python3-dev libffi-dev openssl-dev build-base

# set python path and working directory
WORKDIR /opt/wordofthedaytelegrambot

# copy application and install requirements.txt dependencies
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# run application
CMD ["/usr/bin/python3", "/opt/wordofthedaytelegrambot/main.py"]