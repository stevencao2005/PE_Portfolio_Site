#!/bin/bash

#post request
echo "create random timeline using POST endpoint"
curl --request POST http://127.0.0.1:5000/api/timeline_post -d 'name=random&email=random@random.com&content=creating a random timeline post'

#get request
echo "confirm it was added using GET endpoint"
curl http://127.0.0.1:5000/api/timeline_post