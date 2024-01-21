rm -rf ./wordpress
rm -rf ./app
rm -rf ./app.tar.gz
wget https://en-ca.wordpress.org/latest-en_CA.tar.gz -O app.tar.gz
tar -xvzf ./app.tar.gz
rm -rf ./app.tar.gz
mv ./wordpress ./app