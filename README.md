# docker-wordpress

### Installation script

cd into the ```docker-wordpress``` directory, and run:

```
docker run --rm \
--workdir /home/workspace \
--mount type=bind,source=$(pwd),target=/home/workspace \
alpine:latest \
/bin/sh -c \
"rm -rf ./wordpress \
&& rm -rf ./app \
&& rm -rf ./app.tar.gz \
&& wget https://en-ca.wordpress.org/latest-en_CA.tar.gz -O app.tar.gz \
&& tar -xvzf ./app.tar.gz \
&& rm -rf ./app.tar.gz \
&& mv ./wordpress ./app"
```