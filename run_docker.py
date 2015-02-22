#!/bin/bash

docker run -it -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v /dev/dri:/dev/dri -v /dev/snd:/dev/snd --privileged --net=host yoyo 
