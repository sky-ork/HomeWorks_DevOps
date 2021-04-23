#!/usr/bin/env python3
import os
import sys
import subprocess


def check_path(path):
    return subprocess.run(['git', '-C', path, 'status'],
                          stderr=subprocess.STDOUT,
                          stdout=subprocess.DEVNULL).returncode


repo_path = sys.argv[1]
if check_path(repo_path) == 0:
    bash_command = ["cd " + repo_path, "git status"]
    result_os = os.popen(' && '.join(bash_command)).read()
    for result in result_os.split('\n'):
        if result.find('изменено') != -1:
            prepare_result = '   ' + repo_path \
                             + result.replace('\tизменено:      ', '/')
            print(prepare_result)
else:
    print("Указанный путь не является репозиторием")
