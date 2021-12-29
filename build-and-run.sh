#/bin/bash

docker build -t achievement_announcer .
docker stop achievement_announcer > /dev/null 2>&1
docker rm achievement_announcer > /dev/null 2>&1
docker run -d --restart=always --cap-add=SYS_TIME --name achievement_announcer -h achievement_announcer achievement_announcer 
