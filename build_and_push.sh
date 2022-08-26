#!/usr/bin/env bash

account=$1
image=$2
path=$3

if [ "$account" == "" ] || [ "$image" == "" ] || [ "$path" == "" ]
then
    echo "Usage: $0 <account> <image-name> <path>"
    exit 1
fi

# Dockerイメージをビルド
docker build -t ${image} app/. -f ${path}

# Docker Hubにプッシュ
docker tag ${image} ${account}/${image}
docker login
docker push ${account}/${image}