# Format: FROM    repository[:version]
FROM ubuntu:17.04
FROM python:3.6
MAINTAINER Geoffrey 'geoffrey.geofe@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
EXPOSE 80
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]