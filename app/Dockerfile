FROM python:3.9-alpine
RUN apk add --no-cache bash

# copy project
COPY ./ ./app
# set work directory
WORKDIR ./app
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt