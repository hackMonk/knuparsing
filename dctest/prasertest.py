# -*- coding: cp949 -*-
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
            print('thew new update is', blist[i])
            diff = 1
            return diff;
    return diff

def updateFile():
    fu = open("update.txt", "w+")
    target_url = "http://gall.dcinside.com/board/lists/?id=destinychild"
    sauce = uReq(target_url).read().decode('utf-8')
    soup = BeautifulSoup(sauce, 'html.parser')

    for list in soup.find_all('a', {'class':['icon_txt_n', 'icon_pic_n']}):
        try:
            fu.write(list.text+"\n")
        except UnicodeEncodeError:
            continue
    fu.close()

def checkUpdateFile():
    fc = open("check.txt", "w+")
    target_url = "http://gall.dcinside.com/board/lists/?id=destinychild"
    sauce = uReq(target_url).read().decode('utf-8')
    soup = BeautifulSoup(sauce, 'html.parser')

    for list in soup.find_all('a', {'class':['icon_txt_n', 'icon_pic_n']}):
        try:
            fc.write(list.text+"\n")
        except UnicodeEncodeError:
            continue
    fc.close()


if __name__ == "__main__":
    updateCheck = 0
    fc = open("check.txt", "w+")
    fu = open("update.txt", "w+")
    target_url = "http://gall.dcinside.com/board/lists/?id=destinychild"
    sauce = uReq(target_url).read().decode('utf-8')
    soup = BeautifulSoup(sauce, 'html.parser')

    for list in soup.find_all('a', {'class':['icon_txt_n', 'icon_pic_n']}):
        #print(list.text)
        try:
            fc.write(list.text+"\n")
            fu.write(list.text+"\n")
        except UnicodeEncodeError:
            continue
    fc.close()
    fu.close()
        # print(list.text)
    while(1):
        while(updateCheck is 0):
            updateFile()
            updateCheck = check()
            time.sleep(1)
        checkUpdateFile()
        updateCheck = 0
