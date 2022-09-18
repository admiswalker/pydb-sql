#!/bin/bash

SCRIPT_DIR=`cd $(dirname ${BASH_SOURCE:-$0}); pwd`
DOCKER_IMAGE_NAME=`cat ${SCRIPT_DIR}/docker_image_name.txt | tr -d '\r' | tr -d '\n'`

docker run \
       -u `id -u`:`id -g` \
       -v /etc/group:/etc/group:ro \
       -v /etc/passwd:/etc/passwd:ro \
       -v /etc/shadow:/etc/shadow:ro \
       -v /etc/sudoers.d:/etc/sudoers.d:ro \
       --rm -it --name ${DOCKER_IMAGE_NAME} \
       -v $PWD:/home -w /home \
       ${DOCKER_IMAGE_NAME}:latest bash

