#!/bin/bash
set -e
set -x


case "$1" in 
  server)
    echo "$1"
    echo $(pwd)
    uvicorn octoflow.server.main:app ;;
  scheduler)
    echo "$1"
    airflow scheduler ;;
  *)
    echo "${@} is not recognized as a startup command." ;;
esac