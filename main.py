import os
import requests
from bs4 import BeautifulSoup
import re
pattern = re.compile(r'\bcontent=.(.*).\s')
os.chdir("<ADD PATH HERE>")                                                          # HERE WE MOVE THE DIR WHERE videso.txt IS
valuesDic = {}
if __name__ == '__main__':
    with open("<INSERT NAME HERE>", "r") as f:                                                                                  # HERE THE NAME YOU HAVE TO ENTER THE NAME OF THE TXT ARCHIVE THAT yt-dlp GENERATED
        for enum, i in enumerate(f, start=1):

            t = list(map(str, i.split()))
            link = "https://www.youtube.com/watch?v="+t[1]
            r = requests.get(link).text
            soup = BeautifulSoup(r, features="lxml")
            body = soup.find("body")
            div1 = body.find("div", class_="watch-main-col")
            match = pattern.search(str(div1.meta))

            valuesDic[t[1]] = match[1].replace("/", "-")                                                                #WE REPLACE ANY / TO - TO PREVENT ERRORS WHEN RENAMING
            print(f"{enum}: {valuesDic[t[1]]}")


    os.chdir("<ADD PATH HERE>") #WE CHANGE TO THE DIRECTORY WHERE THE VIDEOS TO RENEAME ARE
    for i in os.listdir():
        file_nameOld, file_ext = os.path.splitext(i)
        new_name = valuesDic[file_nameOld]+file_ext
        print(f"key:{file_nameOld}-->>{new_name}")
        os.rename(i, new_name)

