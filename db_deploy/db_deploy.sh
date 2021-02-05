#! /bin/bash

echo "[db_deploy] starting"

docker build -t visa-sponsor-search-db-deploy . 

docker run \
    -it \
    --rm \
    --network=visa-sponsor-search_default \
    visa-sponsor-search-db-deploy
