from sys import argv
from os import mkdir
from collections import deque
import requests

dir_for_tabs = argv[1]

try:
    mkdir(dir_for_tabs)
except FileExistsError:
    print(f"Directory {dir_for_tabs} already exists")

history = deque()

def save_site_content(data, path,extension):

    history.append(path)
    with open(f"./{dir_for_tabs}/{path+'.'+extension}", 'w',encoding = 'UTF-8') as f:
        f.write(data)

def go_site(site,filename):
    address = site if site.startswith("https://") else f"https://{site}"
    response = requests.get(address)
    extension = response.headers['content-type'].split(" ")[0].split("/")[1].replace(";","")
    save_site_content(response.text, filename,extension)

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
      filename = input("Enter filename\n")
      go_site(command,filename)
