import os
import sys
import re
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore


def get_page(url):
    if not re.match(r"^http[s]://", url):
        url = "https://" + url

    response = requests.get(url)
    return response


def parse_page(res):
    text_page = []
    soup = BeautifulSoup(res.content, "html.parser")
    tags = ["p", "h1", "h2", "h3", "h4", "h5", "h6", "a", "ul", "ol", "li"]
    for tag in soup.find_all(tags):
        if tag.name == "a":
            text_page.append(Fore.BLUE + tag.text)
        else:
            text_page.append(tag.text)
    return "\n".join(text_page)


history = deque()

if __name__ == "__main__":
    save_dir = os.getcwd()
    if len(sys.argv) > 1 and sys.argv[1]:
        save_dir = sys.argv[1]
    else:
        save_dir = "default"
    try:
        os.mkdir(save_dir)
    except FileExistsError:
        pass
    site = None
    while True:
        current_page = site
        site = input()
        if site == "exit":
            break

        if site == "back":
            try:
                site = history.pop()
                if site is None:
                    continue
            except IndexError:
                continue
        else:
            history.append(current_page)

        file_path = os.path.join(save_dir, site.split(".", 1)[0])
        if re.match(r"^.+\.", site):
            try:
                res = get_page(site)
                page = parse_page(res)
                print(page)
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(page)
            except KeyError:
                print("Error: Page not found")
                continue
        elif site in os.listdir(save_dir):
            with open(file_path, "r") as file:
                print(file.read())
        else:
            print("Error: Incorrect URL")
            continue
