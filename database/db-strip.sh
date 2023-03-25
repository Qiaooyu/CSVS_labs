#!/bin/bash

./strip-image.sh  \
  -v \
  -i db-final-changefile \
  -t db-strip-test:1 \
  -p mariadb \
  -f /bin/bash \
  -f /bin/ls \
  -f /bin/cd \
  -f /mysql/mysql.conf.d/mysqld.cnf \
  -f /etc/passwd \
  -f /etc/nsswitch.conf \
  -f /etc/host.conf \
  -f /etc/resolv.conf \
  -f /usr/lib/x86_64-linux-gnu \
  -f /usr/local/bin/docker-entrypoint.sh \
  -f /usr/sbin/mariadbd \
  -f /usr/sbin/mysqld \
  -f /usr/lib64/ld-linux-x86-64.so.2 \
  -f /run/mysqld \
  -f /var/lib/mysql \
  -f /tmp \
  -d Dockerfile


# final version
