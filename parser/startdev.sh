#! /bin/bash

docker build -t visa-sponsorship-search-parser . 

docker run \
    --add-host=postgresql:192.168.65.2 \
    --mount source=$HOME/Developer/visa-sponsor-search/visa-sponsor-search/localData,target=/app/localData,type=bind \
    --rm \
    -it \
    visa-sponsorship-search-parser:latest
