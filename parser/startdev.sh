#! /bin/bash

docker build -t visa-sponsor-search-parser . 

docker run \
    --add-host=postgres:192.168.65.2 \
    --mount source=$HOME/Developer/visa-sponsor-search/visa-sponsor-search/localData,target=/app/localData,type=bind \
    --rm \
    -it \
    visa-sponsor-search-parser:latest
