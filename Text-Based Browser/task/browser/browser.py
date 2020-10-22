from sys import argv
from os import mkdir
from collections import deque
import requests

dir_for_tabs = argv[1]

print("Hello world")

try:
    mkdir(dir_for_tabs)
except FileExistsError:
    print(f"Directory {dir_for_tabs} already exists")

history = deque()

def save_site_content(data, path):
    history.append(path)
    with open(f"./{dir_for_tabs}/{path+'.html'}", 'w',encoding = 'UTF-8') as f:
        f.write(data)

def go_site(site):
    address = site if site.startswith("https://") else f"https://{site}"
    site_content = requests.get(address).text
    save_site_content(site_content, site)
    print(site_content)

def go_back():

    with open(f"./{dir_for_tabs}/{history.leftpop()+'.html'}", 'r',encoding = 'UTF-8') as f:
        print(f.read())

while True:
    command = input()

    if command == 'exit':
        break
    elif command =="back":
        go_back()
    elif '.' in command:
        go_site(command)
