import os
import sys
import re
import requests
from collections import deque


def get_page(url):
    if not re.match(r"^http[s]://", url):
        url = "https://" + url

    response = requests.get(url)
    return response.text


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
                # TODO: Request Page
                # page = globals()[site.replace(".", "_")]
                page = get_page(site)
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
