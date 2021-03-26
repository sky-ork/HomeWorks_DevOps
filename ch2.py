#!/usr/bin/env python3
import os

bash_command = ["cd ~/PycharmProjects/Test_DevOps/Test_DevOps", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('изменено') != -1:
        prepare_result = '   ' + bash_command[0].replace('cd ', '')\
                         + '/' + result.replace('\tизменено:      ', '')
        print(prepare_result)
