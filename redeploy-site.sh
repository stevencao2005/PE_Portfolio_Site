#!/bin/bash

#change directory to project folder
cd /root/PE_Portfolio_Site

#get updated changes
git fetch && git reset origin/main --hard

#activate virtual environment and install the suggested dependencies
source python3-virtualenv/bin/actviate
pip install -r requirements.txt

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up --build
