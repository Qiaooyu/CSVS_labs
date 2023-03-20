# database-run

docker run -d \
--net u2239149/csvs2023_n \
--ip 203.0.113.201 \
--hostname db.cyber23.test \
-e MYSQL_ROOT_PASSWORD="CorrectHorseBatteryStaple" \
-e MYSQL_DATABASE="csvs23db" \
--security-opt seccomp=min-db.json \
--security-opt label:type:database_t \
--cap-drop=ALL \
--name db_all \
db_change_dockerfile

docker exec -i db_all mysql -uroot -pCorrectHorseBatteryStaple < sqlconfig/csvs23db.sql

# web-run

docker run -d \
--net u2239149/csvs2023_n \
--ip 203.0.113.200 \
--hostname www.cyber23.test \
--add-host db.cyber23.test:203.0.113.201 \
-p 80:80 \
--security-opt label:type:webserver_t \
--security-opt seccomp=min-web3.json \
--cap-drop=ALL \
--cap-add=CAP_CHOWN \
--cap-add=CAP_NET_BIND_SERVICE \
--cap-add=CAP_SETGID \
--cap-add=CAP_SETUID \
--name web_all \
u2239149/csvs2023-web_i:0.1

docker run -d \
--net u2239149/csvs2023_n \
--ip 203.0.113.200 \
--hostname www.cyber23.test \
--add-host db.cyber23.test:203.0.113.201 \
-p 80:80 \
--security-opt label:type:webserver_t \
--cap-drop=ALL \
--cap-add=CAP_CHOWN \
--cap-add=CAP_NET_BIND_SERVICE \
--cap-add=CAP_SETGID \
--cap-add=CAP_SETUID \
--name web \
u2239149/csvs2023-web_i:0.1