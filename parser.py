from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import time

def check():
    alist = []
    blist = []
    dif = 0
    with open('check.txt') as check:
        for cline in check:
            alist.append(cline)
    with open('update.txt') as update:
        for uline in update:
            blist.append(uline)
    for i in range(len(alist)):
        if set(alist[i]) == set(blist[i]):
            diff = 0
        else:
            diff = 1
            break
    return diff

def updateFile():
    fu = open("update.txt", "w+")
    target_url = "http://computer.knu.ac.kr/07_sub/01_sub.html"
    sauce = uReq(target_url).read()
    soup = BeautifulSoup(sauce, 'html.parser')
    anchors = soup.find_all('a', {'href' : True})
    for anchor in anchors:
        title = anchor.get('title')
        if title:
            fu.write(title+"\n")

def checkUpdateFile():
    fc = open("update.txt", "w+")
    target_url = "http://computer.knu.ac.kr/07_sub/01_sub.html"
    sauce = uReq(target_url).read()
    soup = BeautifulSoup(sauce, 'html.parser')
    anchors = soup.find_all('a', {'href' : True})
    for anchor in anchors:
        title = anchor.get('title')
        if title:
            fc.write(title+"\n")

if __name__ == "__main__":
    updateCheck = 1
    fc = open("check.txt", "w+")
    fu = open("update.txt", "w+")
    target_url = "http://computer.knu.ac.kr/07_sub/01_sub.html"
    sauce = uReq(target_url).read()
    soup = BeautifulSoup(sauce, 'html.parser')
    anchors = soup.find_all('a', {'href' : True})
    for anchor in anchors:
        title = anchor.get('title')
        if title:
            fc.write(title+"\n")
            fu.write(title+"\n")
    fc.close()
    fu.close()
    updateCheck = check()

    while(1):
        while(updateCheck == 0):
            updateFile()
            updateCheck = check()
            print("Loop One")
            time.sleep(10)
        print("there is a new update")
        checkUpdateFile()
