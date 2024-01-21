# docker-wordpress

With ```docker``` and ```docker-compose``` installed, cd into the ```docker-wordpress``` directory and run the following steps:

### Step 1 - Install wp-config.php

```
docker run --rm \
--workdir /home/workspace \
--mount type=bind,source=$(pwd),target=/home/workspace \
python:3 \
/bin/bash -c "pip install requests && python3 ./docker/wp-config-install.py"
```

### Step 2 - Download and install WordPress

```
chmod 777 ./docker/wp-install.sh && \
docker run --rm \
--workdir /home/workspace \
--mount type=bind,source=$(pwd),target=/home/workspace \
alpine:latest \
/bin/sh -c "./docker/wp-install.sh"
```

### Step 3 - Run your WordPress website

```
docker-compose up -d
```