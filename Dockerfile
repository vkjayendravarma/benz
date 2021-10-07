FROM ubuntu:20.04
LABEL maintainer="Jayendra Varma<vkjayendravarma@gmail.com>"

RUN apt-get update
RUN apt-get -y install python3.8 
RUN apt-get -y install python3-pip

FROM python:3.8.5-slim-buster
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0" ,"--port=5000"]