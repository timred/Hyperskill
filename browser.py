import os
import sys
import re

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

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
    while True:
        site = input()
        if site == "exit":
            break

        file_path = os.path.join(save_dir, site.split(".", 1)[0])
        if re.match(r"^.+\.", site):
            site = site.replace(".", "_")
            try:
                page = globals()[site]
                print(page)
                with open(file_path, "w") as file:
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
