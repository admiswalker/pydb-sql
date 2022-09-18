#!/bin/bash

TARGET='pytest -s'
if [ $# != 1 ]; then
    echo 'RUN: '${TARGET}
else
    TARGET=$1
    echo 'RUN: '${TARGET}
fi

SCRIPT_DIR=`cd $(dirname ${BASH_SOURCE:-$0}); pwd`
DOCKER_IMAGE_NAME=`cat ${SCRIPT_DIR}/docker/docker_image_name.txt | tr -d '\r' | tr -d '\n'`

docker run \
       -u `id -u`:`id -g` \
       --rm -it --name ${DOCKER_IMAGE_NAME} \
       -v $PWD:/home -w /home \
       --network host \
       ${DOCKER_IMAGE_NAME}:latest ${TARGET}

