import random
import string
import urllib.parse
import urllib.request
import json
import subprocess
import time


def func_test():
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


if __name__ == '__main__':
    with open('/home/csc//Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/moby-syscalls') as f:
        syscalls = [l.strip() for l in f.readlines()]
    for s in syscalls:
        with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/moby-default.json') as f:
            json_data = json.load(f)
        print(f"{s} being removed from moby-default.json")
        json_data['syscalls'][0]['names'].remove(s)
        tmp_file = '/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/tmp.json'
        with open(tmp_file, 'w') as f:
            json.dump(json_data, f)

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
        except:
            subprocess.run(kill_command, shell=True)
            print("test failed and docker killed")
            with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/list-of-min-syscalls',
                      'a') as f:
                f.write(f"{s}\n")

        # try:
        #     run_result = subprocess.run(run_command, shell=True, check=True)
        #     print(run_result.returncode)
        # except subprocess.SubprocessError as e:
        #     print(e)
        #     with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/list-of-min-syscalls',
        #               'a') as f:
        #         f.write(f"{s}\n")
        # else:
        #     print("docker run failed and ")
        #
        # time.sleep(2)
        # print("sleep 2s")
        #
        # try:
        #     func_test_result = func_test()
        #     print(func_test_result)
        # except Exception as e:
        #     if e == "fail-3" or "fail-2" or "fail-1":
        #         print("function test failed and errcode = ", e)
        #         with open('/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/list-of-min-syscalls',
        #                   'a') as f:
        #             f.write(f"{s}\n")
        #         subprocess.run(kill_command, shell=True)
        #
        # try:
        #     run_result = subprocess.run(kill_command, shell=True)
        #     print(run_result.returncode)
        # except