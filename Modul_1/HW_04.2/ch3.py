#!/usr/bin/env python3
import os
import sys

repo_path = sys.argv[1]
bash_command = ["cd " + repo_path, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('изменено') != -1:
        prepare_result = '   ' + repo_path \
                         + result.replace('\tизменено:      ', '/')
        print(prepare_result)
