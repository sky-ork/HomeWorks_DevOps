#!/usr/bin/env python3
import os

repo_path = "~/PycharmProjects/HomeWorks_DevOps/HomeWorks_DevOps"
bash_command = ["cd " + repo_path, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('изменено') != -1:
        prepare_result = bash_command[0].replace('cd ', '   ') \
                         + result.replace('\tизменено:      ', '/')
        print(prepare_result)
