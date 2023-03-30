docker run -d \
--net u2239149/csvs2023_n \
--ip 203.0.113.201 \
--hostname db.cyber23.test \
-e MYSQL_ROOT_PASSWORD="CorrectHorseBatteryStaple" \
-e MYSQL_DATABASE="csvs23db" \
--security-opt seccomp=min-db.json \
--security-opt label:type:database_t \
--cap-drop=ALL \
-v mydata:/var/lib/mysql:Z \
--name db-all-strip \
db-strip-test:1




docker run -d \
--net u2239149/csvs2023_n \
--ip 203.0.113.200 \
--hostname www.cyber23.test \
--add-host db.cyber23.test:203.0.113.201 \
-p 80:80 \
--security-opt label:type:webserver_t \
--security-opt seccomp=min-web5.json \
--cap-drop=ALL \
--cap-add=CAP_CHOWN \
--cap-add=CAP_NET_BIND_SERVICE \
--cap-add=CAP_SETGID \
--cap-add=CAP_SETUID \
--name web-all-strip \
web-strip-test:2.2



