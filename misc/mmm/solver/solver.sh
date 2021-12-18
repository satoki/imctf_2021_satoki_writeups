#!/bin/bash

URL="http://118.27.114.90:31417"
#URL="http://118.27.104.46:31417"
wget "$URL/5353" &
curl "$URL/?data=local"