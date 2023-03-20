#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
import tarfile


def debug(*args):
    print('DEBUG:', *args, file=sys.stderr)


def debug_break(*args):
    debug(*args)
    sys.exit(3)


def usage_c():
    script_name = os.path.basename(__file__)
    print(f'usage: {script_name} [-v] [-d export-dir] [-p package|-f file]', file=sys.stderr)


def usage_h():
    script_name = os.path.basename(__file__)
    print(f'usage: {script_name} -i image-name -t stripped-image-name [-t stripped-image-name] [-d Dockerfile] '
          f'[-p package|-f file] [-v]', file=sys.stderr)


def parse_commandline_c():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', action='store_true')
    parser.add_argument('-p', dest='packages', action='append', default=[])
    parser.add_argument('-f', dest='files', action='append', default=[])
    parser.add_argument('-d', dest='export_dir', required=True)
    parser.add_argument('-u', dest='chown_uid')
    args = parser.parse_args()

    if not os.path.isdir(args.export_dir):
        usage_c()
        print(f'{args.export_dir} is not a directory.', file=sys.stderr)
        sys.exit(22)

    if not args.packages and not args.files:
        usage_c()
        print('Missing -p or -f options', file=sys.stderr)
        sys.exit(23)

    return args


def print_file_c(file_path):
    if os.path.exists(file_path):
        print(file_path)
    elif args.v:
        print(f"INFO: ignoring not existent file '{file_path}'", file=sys.stderr)

    if os.path.getsize(file_path):
        target = os.readlink(file_path)
        if target:
            if target.startswith('/'):
                list_dependencies_c(target)
            else:
                list_dependencies_c(os.path.join(os.path.dirname(file_path), target))


def list_dependencies_c(*files):
    for file_path in files:
        if os.path.exists(file_path):
            print_file_c(file_path)
            if subprocess.call(['/usr/bin/ldd', file_path], stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL) == 0:
                ldd_output = subprocess.check_output(['/usr/bin/ldd', file_path]).decode()
                for line in ldd_output.splitlines():
                    if 'statically' in line:
                        continue
                    words = line.split()
                    if len(words) >= 3:
                        dep_path = words[2]
                        if dep_path.startswith('/'):
                            list_dependencies_c(dep_path)
                        else:
                            list_dependencies_c(os.path.join(os.path.dirname(file_path), dep_path))

        elif args.v:
            print(f"INFO: ignoring not existent file {file_path}", file=sys.stderr)


def list_packages_c(*sources):
    for file_path in sources:
        if not os.path.isdir(file_path):
            list_dependencies_c(file_path)





