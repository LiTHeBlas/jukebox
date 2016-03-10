FROM armbuild/ubuntu-debootstrap:wily
MAINTAINER Olle Vidner <olle@vidner.se>

ENV DEBIAN_FRONTEND=noninteractive
RUN sed -i 's/mirror.cloud.online.net/ports.ubuntu.com/' /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-pip \
    python3.5-dev \
    && rm -rf /var/lib/apt/lists/*

RUN ln -fs /usr/bin/python3.5 /usr/bin/python3

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["python3", "main.py"]
