from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import time

if __name__ == "__main__":
    updateCheck = 1
    fc = open("check.txt", "w+")
    fu = open("update.txt", "w+")
    target_url = "http://gall.dcinside.com/board/lists/?id=superidea"
    sauce = uReq(target_url).read()
    soup = BeautifulSoup(sauce, 'html.parser')

    for list in soup.find_all('b'):
        print(list.text)
        print(list.text)
    fc.close()
    fu.close()
    updateCheck = check()

    # while(1):
    #     while(updateCheck == 0):
    #         updateFile()
    #         updateCheck = check()
    #         print("Loop One")
    #         time.sleep(10)
    #     print("there is a new update")
    #     checkUpdateFile()
