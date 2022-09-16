FROM ubuntu:22.04

# Avoid timezone selection
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN python3.10 -m pip install -r ./requirements.txt \
    ; rm requirements.txt

