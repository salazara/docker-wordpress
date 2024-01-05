FROM php:8.2-apache

RUN apt-get -y update \
&& apt-get -y install apache2-utils \
&& apt-get -y install git \
&& apt-get -y install zip \
&& docker-php-ext-install mysqli pdo pdo_mysql

RUN a2enmod rewrite