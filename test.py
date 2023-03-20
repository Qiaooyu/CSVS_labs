import random
import string
import urllib.parse
import urllib.request
import json
import subprocess
import time

import docker

from all_code_new import func_test

# client = docker.from_env()

tmp_file = '/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/tmp2.json'

run_command = f"docker run -d --rm \
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
           --security-opt seccomp={tmp_file} \
           --name webtest \
           u2239149/csvs2023-web_i:0.1"
# try:
#     client.containers.run("u2239149/csvs2023-web_i:0.1", detach=True, network="u2239149/csvs2023_n", hostname="www.cyber23.test",
#                           extra_hosts="db.cyber23.test:203.0.113.201", ports={'80/tcp': 80},
#                           security_opt=["label:type:webserver_t"], cap_drop="ALL",
#                           cap_add="CAP_CHOWN,CAP_NET_BIND_SERVICE,CAP_SETGID,CAP_SETUID",
#                           name="webtest")
# except Exception as e:
#     print(e)





run_command = f"docker run -d --rm \
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
    --security-opt seccomp={tmp_file} \
    --name webtest \
    u2239149/csvs2023-web_i:0.1"

kill_command = "docker kill webtest"

try:
    run_result = subprocess.run(run_command, shell=True, check=True)
    print(run_result.returncode)
    time.sleep(2)
    print("sleep 2s")
    func_test_result = func_test()
    print(func_test_result)
    run_result = subprocess.run(kill_command, shell=True)
    print(run_result.returncode)
except Exception as e:
    if e == "fail-3" or "fail-2" or "fail-1":
        print("function test failed and errcode = ", e)
        with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/list-of-min-syscalls',
                  'a') as f:
            f.write("6987\n")
    else:
        print(e)