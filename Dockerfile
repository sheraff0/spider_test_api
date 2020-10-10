FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# Geospatial libraries
RUN apt update && \
    apt -y install binutils libproj-dev gdal-bin && \
    apt clean