import time
from datetime import datetime as dt


hosts_temp='hosts' #copy to current directory for testing: cp /etc/hosts hosts
hosts_path='/etc/hosts' 
redirect='127.0.0.1'
website_lists=['www.facebook.com','facebook.com','instagram.com','www.instagram.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        with open(hosts_path, 'r+') as hosts_file:
            hosts = hosts_file.read()
            for website in website_lists:
                if website in hosts:
                    pass
                else:
                    hosts_file.write(redirect + ' ' + website + '\n')
    else:
        with open(hosts_path, 'r+') as reverse_hosts_file:
            line = reverse_hosts_file.readlines()
            reverse_hosts_file.seek(0)
            for i in line:
                if not any (website in i for website in website_lists):
                    reverse_hosts_file.write(i)
            reverse_hosts_file.truncate()
        print('Fun hours...')
    time.sleep(5)
