#!/bin/bash

SCRIPT_DIR=`cd $(dirname ${BASH_SOURCE:-$0}); pwd`
DOCKER_IMAGE_NAME=`cat ${SCRIPT_DIR}/docker_image_name.txt | tr -d '\r' | tr -d '\n'`

docker run \
       --rm -it --name ${DOCKER_IMAGE_NAME} \
       ${DOCKER_IMAGE_NAME}:latest bash
