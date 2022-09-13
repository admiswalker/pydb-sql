FROM ubuntu:22.04

# Avoid timezone selection
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3.10 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

