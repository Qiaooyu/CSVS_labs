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