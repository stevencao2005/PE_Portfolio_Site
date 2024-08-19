#!/bin/bash

#change directory to project folder
cd /root/PE_Portfolio_Site

#get updated changes
git fetch && git reset origin/main --hard

# Stop and remove all running containers, networks, and volumes defined in the production Docker Compose file,
# then rebuild and start the containers using the updated production configuration.
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up --build
