#!/bin/bash

#change directory to project folder
cd /root/PE_Portfolio_Site

#get updated changes
git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build
