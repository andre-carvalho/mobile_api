#!/bin/bash

docker run -p 5000:5000 -v /home/andre/Documents/upload_docker_files:/server/utils/uploadImages --name upload-server --rm \
--env HOST=192.168.1.121 --env PORT=5432 --env DBNAME=upload --env DBUSER=postgres --env DBPASS=postgres \
-d upload-server:v2
