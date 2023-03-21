import subprocess
import time

from find_cap import timeout






run_command = 'docker run -d --rm ' \
                      '--net u2239149/csvs2023_n --ip 203.0.113.201 --hostname db.cyber23.test ' \
                      '-e MYSQL_ROOT_PASSWORD="CorrectHorseBatteryStaple" -e MYSQL_DATABASE="csvs23db" ' \
                      '--security-opt seccomp=/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/db_test_case/tmp.json ' \
                      '--name dbtest ' \
                      'u2239149/csvs2023-db_i:0.1'

mysql_command = 'docker exec -i dbtest mysql -uroot -pCorrectHorseBatteryStaple < ' \
                '/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/dbserver/sqlconfig/csvs23db.sql'



@timeout(60)
def run():
    try:
        subprocess.check_output(run_command, shell=True)
        time.sleep(5)
        try:
            mysql_command_result = subprocess.check_output(mysql_command, shell=True)
            print(mysql_command_result.decode())
            print("command success")
        except subprocess.SubprocessError as e:
            print(e)
    except TimeoutError:
        print(1)

run()
