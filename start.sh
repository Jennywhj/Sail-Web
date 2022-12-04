#!/bin/bash
app="deepstream-mri"
username="yangyanting"

case "$1" in
    "debug")
        docker stop ${app}-debug
        docker rm ${app}-debug
        docker build -t ${app}:debug .
        docker image prune -f
        docker run -p 127.0.0.1:5000:5000 --name=${app}-debug ${app}:debug
        ;;
    "pull_run")
        docker pull ${username}/${app}
        docker stop ${app}
        docker rm ${app}
        docker image prune -f
        docker run --init -d -p 127.0.0.1:5000:5000 --name=${app} ${username}/${app}
        ;;
esac


