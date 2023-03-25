import random
import string
import urllib.parse
import urllib.request
import json
import subprocess
import time
import docker

client = docker.from_env()
with open('/home/csc//Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/access/moby-syscalls') as f:
    syscalls = [l.strip() for l in f.readlines()]
for s in syscalls:
    with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/access/moby-default.json') as f:
        json_data = json.load(f)
    print(f"{s} being removed from moby-default.json")
    json_data['syscalls'][0]['names'].remove(s)
    tmp_file = '/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/access/tmp.json'
    with open(tmp_file, 'w') as f:
        json.dump(json_data, f)


    container = client.containers.run(

    )



    container_id =  client.containers.get(container.id)