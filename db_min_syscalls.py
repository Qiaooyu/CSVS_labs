import json
import subprocess
import time

from func_timeout import timeout
from web_min_syscalls import func_test


@timeout(30)
def mysql_command_run(mysql_command):
    try:
        try:
            mysql_command_result = subprocess.check_output(mysql_command, shell=True)
            print(mysql_command_result.decode())
            return "mysql command success"
        except subprocess.SubprocessError:
            raise Exception("mysql command failed")
    except TimeoutError:
        raise Exception("mysql command timeout")


if __name__ == '__main__':
    # start reduce min syscalls base on min-db.json which is generated for db_min_syscalls.py
    with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/db_test_case/min_syscalls_1') as f:
        syscalls = [l.strip() for l in f.readlines()]
    for s in syscalls:
        with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/db_test_case/min-db.json') as f:
            json_data = json.load(f)
        print(f"{s} being removed from min-db.json")
        json_data['syscalls'][0]['names'].remove(s)
        tmp_file = '/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/db_test_case/tmp.json'
        with open(tmp_file, 'w') as f:
            json.dump(json_data, f)

        run_command = 'docker run -d --rm ' \
                      '--net u2239149/csvs2023_n --ip 203.0.113.201 --hostname db.cyber23.test ' \
                      '-e MYSQL_ROOT_PASSWORD="CorrectHorseBatteryStaple" -e MYSQL_DATABASE="csvs23db" ' \
                      '--security-opt seccomp=/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/db_test_case/tmp.json ' \
                      '--security-opt label:type:database_t ' \
                      '--cap-drop=ALL ' \
                      '--name dbtest ' \
                      'u2239149/csvs2023-db_i:0.1'

        mysql_command = 'docker exec -i dbtest mysql -uroot -pCorrectHorseBatteryStaple < ' \
                        '/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/dbserver/sqlconfig/csvs23db.sql'

        kill_command = 'docker kill dbtest'
        try:
            subprocess.run(run_command, shell=True, check=True)
            print("run success")
            time.sleep(5)
            print("sleep 5s")
            mysql_command_run(mysql_command)
            print("mysql command success")
            func_test()
            print("func_test success")
            subprocess.run(kill_command, shell=True)
            print("docker killed")
        except:
            print("test failed")
            subprocess.run(kill_command, shell=True)
            print("docker killed")
            with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/db_test_case/list-of-min-syscalls',
                      'a') as f:
                f.write(f"{s}\n")

# if __name__ == '__main__':
#     with open('/home/csc//Desktop/PMA-start/2023-02-06.csvs.rc1/db_test_case/moby-syscalls') as f:
#         syscalls = [l.strip() for l in f.readlines()]
#     for s in syscalls:
#         with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/db_test_case/moby-default.json') as f:
#             json_data = json.load(f)
#         print(f"{s} being removed from moby-default.json")
#         json_data['syscalls'][0]['names'].remove(s)
#         tmp_file = '/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/db_test_case/tmp.json'
#         with open(tmp_file, 'w') as f:
#             json.dump(json_data, f)
#
#         run_command = 'docker run -d --rm ' \
#                       '--net u2239149/csvs2023_n --ip 203.0.113.201 --hostname db.cyber23.test ' \
#                       '-e MYSQL_ROOT_PASSWORD="CorrectHorseBatteryStaple" -e MYSQL_DATABASE="csvs23db" ' \
#                       '--security-opt seccomp=/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/db_test_case/tmp.json ' \
#                       '--name dbtest ' \
#                       'u2239149/csvs2023-db_i:0.1'
#
#         mysql_command = 'docker exec -i dbtest mysql -uroot -pCorrectHorseBatteryStaple < ' \
#                         '/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/dbserver/sqlconfig/csvs23db.sql'
#
#         kill_command = 'docker kill dbtest'
#         try:
#             subprocess.run(run_command, shell=True)
#             print("run success")
#             time.sleep(5)
#             print("sleep 5s")
#             mysql_command_run()
#             print("mysql command success")
#             func_test()
#             print("func_test success")
#             subprocess.run(kill_command, shell=True)
#             print("docker killed")
#         except:
#             print("test failed")
#             subprocess.run(kill_command, shell=True)
#             print("docker killed")
#             with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/db_test_case/list-of-min-syscalls',
#                       'a') as f:
#                 f.write(f"{s}\n")
