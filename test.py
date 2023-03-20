import subprocess

tmp_file = "/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/web_test_case/tmp-bind.json"

run_command = f"docker run -d --rm \
            --net u2239149/csvs2023_n \
            --ip 203.0.113.203 \
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
            --name webtest-bind \
            u2239149/csvs2023-web_i:0.1"

subprocess.run(run_command, shell=True, check=True)


