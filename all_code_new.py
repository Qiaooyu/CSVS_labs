import functools
import signal
import random
import string
import urllib.parse
import urllib.request
import json
import subprocess
import time


def timeout(sec):
    """
    timeout decorator
    :param sec: function raise TimeoutError after ? seconds
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):

            def _handle_timeout(signum, frame):
                err_msg = f'Function {func.__name__} timed out after {sec} seconds'
                raise TimeoutError(err_msg)

            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(sec)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapped_func

    return decorator


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


@timeout(30)
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


def docker_run(command):
    try:
        subprocess.run(command, check=True, shell=True)
        print("docker run success")
    except subprocess.CalledProcessError:
        raise Exception("docker run failed")
    else:
        raise Exception("docker run error")


def docker_kill(command):
    try:
        subprocess.run(command, check=True, shell=True)
        print("docker kill success")
    except subprocess.CalledProcessError:
        raise Exception("docker kill failed")
    else:
        raise Exception("docker kill error")


if __name__ == '__main__':
    all_cap = ["cap_chown",
               "cap_dac_override",
               "cap_dac_read_search",
               "cap_fowner",
               "cap_fsetid",
               "cap_kill",
               "cap_setgid",
               "cap_setuid",
               "cap_setpcap",
               "cap_linux_immutable",
               "cap_net_bind_service",
               "cap_net_broadcast",
               "cap_net_admin",
               "cap_net_raw",
               "cap_ipc_lock",
               "cap_ipc_owner",
               "cap_sys_module",
               "cap_sys_rawio",
               "cap_sys_chroot",
               "cap_sys_ptrace",
               "cap_sys_pacct",
               "cap_sys_admin",
               "cap_sys_boot",
               "cap_sys_nice",
               "cap_sys_resource",
               "cap_sys_time",
               "cap_sys_tty_config",
               "cap_mknod",
               "cap_lease",
               "cap_audit_write",
               "cap_audit_control",
               "cap_setfcap",
               "cap_mac_override",
               "cap_mac_admin",
               "cap_syslog"]

    mysql_command = 'docker exec -i dbtest_cap mysql -uroot -pCorrectHorseBatteryStaple < ' \
                    '/home/csc/Desktop/PMA-start/2023-02-06.csvs.rc1/dbserver/sqlconfig/csvs23db.sql'

    useful_cap = []

    kill_command = 'docker kill dbtest_cap'

    for i in range(len(all_cap)):
        run_command = 'docker run -d --rm --cap-drop=ALL --cap-add=' \
                      + (all_cap[i]) + ' --net u2239149/csvs2023_n ' \
                        '--ip 203.0.113.201 '\
                        '--hostname db.cyber23.test ' \
                        '-e MYSQL_ROOT_PASSWORD="CorrectHorseBatteryStaple"  '\
                        '-e MYSQL_DATABASE="csvs23db" '\
                        '--name dbtest_cap '\
                        'u2239149/csvs2023-db_i:0.1'
        print(run_command)
        docker_run(run_command)
        print('success')
        time.sleep(5)
        mysql_command_run(mysql_command)
        print('mysql command success')

        j = 0
        while j < 100:
            try:
                func_test()
                j += 1
            except Exception as e:
                useful_cap.append(all_cap[i])
                break

        docker_kill(kill_command)

    print(useful_cap)