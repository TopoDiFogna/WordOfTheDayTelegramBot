FROM alpine:3.9.2

# install system dependencies
RUN apk update && apk add python3 python3-dev libffi-dev openssl-dev build-base tzdata

# set python path and working directory
WORKDIR /opt/wordofthedaytelegrambot

# copy application and install requirements.txt dependencies
COPY . .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
RUN cp /usr/share/zoneinfo/Europe/Rome /etc/localtime

# run application
CMD ["/usr/bin/python3", "/opt/wordofthedaytelegrambot/main.py"]