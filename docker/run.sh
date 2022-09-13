#!/bin/bash
docker run \
       -u `id -u`:`id -g` \
       -v /etc/group:/etc/group:ro \
       -v /etc/passwd:/etc/passwd:ro \
       -v /etc/shadow:/etc/shadow:ro \
       -v /etc/sudoers.d:/etc/sudoers.d:ro \
       --rm -it --name docker_py_dev_env_template \
       -v $PWD:/home -w /home \
       docker_py_dev_env_template:latest bash
