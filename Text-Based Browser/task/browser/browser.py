from sys import argv
from os import mkdir
from collections import deque
import requests
from bs4 import BeautifulSoup
import colorama
import re

dir_for_tabs = argv[1]

try:
    mkdir(dir_for_tabs)
except FileExistsError:
    print(f"Directory {dir_for_tabs} already exists")

history = deque()

def parse_html(html_file):

    soup = BeautifulSoup(html_file, 'html.parser')
    webpage_text = []
    tags = soup.find_all(['a','title','ul', 'ol' ,'li','p'])
    for tag in tags:
        if tag.name == 'a':
            webpage_text.append(colorama.Fore.BLUE + tag.text)
        else:
            webpage_text.append("\t"+colorama.Fore.WHITE + re.sub("\n" ," ",re.sub("\s+\|","|", tag.text).strip()))
    print(len(webpage_text))
    return "\n".join(webpage_text)


def print_webpage(webpage):
    colorama.init()
    print(webpage)


def save_site_content(data, path):
    history.append(path)
    with open(f"./{dir_for_tabs}/{path + '.html'}", 'w', encoding='UTF-8') as f:
        colorama.init()
        f.write(data)


def go_site(site):
    address = site if site.startswith("https://") else f"https://{site}"
    site_content = requests.get(address).text
    parse = parse_html(site_content)
    save_site_content(parse, site)
    print_webpage(parse)


def go_back():
    with open(f"./{dir_for_tabs}/{history.leftpop() + '.html'}", 'r', encoding='UTF-8') as f:
        print(f.read())


while True:
    command = input()

    if command == 'exit':
        break
    elif command == "back":
        go_back()
    elif '.' in command:
        go_site(command)
