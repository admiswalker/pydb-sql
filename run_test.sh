#!/bin/bash

TARGET='pytest -s'
if [ $# != 1 ]; then
    echo 'RUN: '${TARGET}
else
    TARGET=$1
    echo 'RUN: '${TARGET}
fi

# run SQL server on docker
DOCKER_IMAGE_NAME='mysql'
#DOCKER_PS=$(docker ps | grep ${DOCKER_IMAGE_NAME})
DOCKER_NUM=$(docker ps | grep -c ${DOCKER_IMAGE_NAME})

if [ ${DOCKER_NUM} -eq 0 ]; then
    # When the SQL server is not started
   ./docker_srv/docker_run_mysql.sh
fi

# run pytest on docker
SCRIPT_DIR=`cd $(dirname ${BASH_SOURCE:-$0}); pwd`
DOCKER_IMAGE_NAME=`cat ${SCRIPT_DIR}/docker/docker_image_name.txt | tr -d '\r' | tr -d '\n'`

docker run \
       -u `id -u`:`id -g` \
       --rm -it --name ${DOCKER_IMAGE_NAME} \
       -v $PWD:/home -w /home \
       --network host \
       ${DOCKER_IMAGE_NAME}:latest ${TARGET}

