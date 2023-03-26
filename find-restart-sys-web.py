import random
import string
import urllib.parse
import urllib.request
import json
import subprocess
import time
import docker


def func_test(fun):
    try:
        # Generate random input data
        fullname = ''.join(random.choices(string.ascii_letters, k=10))
        suggestion = ''.join(random.choices(string.ascii_letters, k=20))
        # print(fullname,suggestion)
        # Encode data for POST request
        data = urllib.parse.urlencode({'fullname': fullname, 'suggestion': suggestion}).encode('utf-8')

        # Call action.php to insert data
        request = urllib.request.Request('http://localhost/action.php', data=data, method='POST')
        # print(request)
        response = urllib.request.urlopen(request, timeout=10)
        print(response.getcode())
        # Check if insert was successful
        if response.getcode() == 403:
            with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/access/403.txt', 'a') as b:
                b.write(f"{fun}\n")
            raise Exception("access denied")
        if response.getcode() == 200:
            # Call index.php to search for new record
            data = urllib.parse.urlencode({'search_fullname': fullname, 'search_suggestion': suggestion}).encode(
                'utf-8')
            request = urllib.request.Request('http://localhost/index.php', data=data, method='GET')
            result = urllib.request.urlopen(request).read().decode('utf-8')
            if fullname in result and suggestion in result:
                return "success"
            else:
                raise Exception("fail-1")
        else:
            raise Exception("fail-2")
    except:
        raise Exception("fail-3")


client = docker.from_env()
with open('/home/csc//Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/access/useless-syscalls') as f:
    syscalls = [l.strip() for l in f.readlines()]
for s in syscalls:
    with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/access/moby-default.json') as f:
        json_data = json.load(f)
    print(f"{s} being removed from moby-default.json")

    json_data['syscalls'][0]['names'].remove(s)
    tmp_file = '/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/access/tmp.json'

    with open(tmp_file, 'w') as f:
        json.dump(json_data, f)

    run_command = f"docker run -d \
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
                web-strip-test:2.2"

    kill_command = "docker kill webtest"

    rm_command = "docker rm webtest"

    try:
        run_result = subprocess.run(run_command, shell=True, check=True)
        print("run_code is ", run_result.returncode)
        time.sleep(0.5)

        a = client.containers.get('webtest')

        a.stop()
        a.start()

        if "FPM initialization failed" in a.logs().decode('utf-8'):
            print("Find it:",s)
            with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/access/restart',
                      'a') as f:
                f.write(f"{s}\n")

        a1 = client.containers.get("webtest").status
        if a1 == "exited":
            print("The status is exited", s)
            with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/access/restart2',
                      'a') as f:
                f.write(f"{s}\n")

        a.kill()
        a.remove()

    except:
        print("## run failed ##")
        subprocess.run(kill_command, shell=True)
        print(" docker killed")
        subprocess.run(rm_command, shell=True)
        print(" docker removed")
        with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/access/restart',
                  'a') as f:
            f.write(f"{s}\n")
