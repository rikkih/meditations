#!/bin/bash

app="meditations"

sudo docker build -t ${app} .
sudo docker run -d -p 5000:5000 \
	--name=${app} \
	-v $PWD:/home/app/${app} ${app}
