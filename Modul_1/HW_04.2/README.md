## Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

1. Скрипт:

    ```python
    #!/usr/bin/env python3
    a = 1
    b = '2'
    c = a + b
    ```
   - будет ошибка при попытке выполнения операции сложения значений типов int и str.
   - Изменить: `a = '1'`
   - Изменить: `b = 2`
    
1. Результат:

   ```python
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
   ```
   
1. Результат:

   ```python
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
   ```
   
1. Результат:

   ```python
   #!/usr/bin/env python3
   import sys
   import socket
   import subprocess
   
   
   # The function returns the URL availability execution code.
   def check_url(url):
       return subprocess.run(['curl', '-Is', url],
                             stdout=subprocess.DEVNULL).returncode
   
   
   # The function returns an array of the dictionary type in the form
   # {<URL>: <IP>,....}. Argument: an array of the URL list type.
   def get_url_ip(url_list):
       url_ip = {}
       len_url_list = len(url_list)
       for count in range(len_url_list):
           # Checking the existence of a URL
           if check_url(url_list[count]) == 0:
               # Checking the availability of an existing URL and
               # and form an array
               while True:
                   try:
                       url_ip[str(url_list[count])] = socket.gethostbyname(str(url_list[count]))
                       break
                   except Exception:
                       continue
       return dict(url_ip)
   
   
   cnt_ask = 0
   print('-' * 40)
   while True:
       if cnt_ask == 0:
           # We get and output the first result without comparing the IP
           url_ip_dict = get_url_ip(sys.argv)
           for item_key in url_ip_dict.keys():
               result = item_key + " - " + url_ip_dict[item_key]
               print(result)
           url_ip_dict_coll = url_ip_dict
           cnt_ask = 1
       else:
           # We get and output the result after comparing the IP
           while True:
               try:
                   url_ip_dict = get_url_ip(sys.argv)
                   break
               except Exception:
                   continue
           for item_key in url_ip_dict.keys():
               if url_ip_dict[item_key] == url_ip_dict_coll[item_key]:
                   result = item_key + " - " + url_ip_dict[item_key]
                   print(result)
               else:
                   result = "[ERROR] " + item_key + " IP mismatch: " \
                            + url_ip_dict_coll[item_key] + " --> " \
                            + url_ip_dict[item_key]
                   print(result)
                   url_ip_dict_coll = url_ip_dict
       print('-' * 40)
   ```