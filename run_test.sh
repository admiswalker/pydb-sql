#!/bin/bash

TARGET=./test/runner.py
if [ $# != 1 ]; then
    echo 'RUN: ./test/runner.py'
else
    TARGET=$1
    echo 'RUN: '${TARGET}
fi

docker run \
       -u `id -u`:`id -g` \
       --rm -it --name docker_py_dev_env_template \
       -v $PWD:/home -w /home \
       docker_py_dev_env_template:latest python3.10 ${TARGET}
