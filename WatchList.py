#########################################
#### File Name : WatchList.py 
#### Path : . 
#### Author SHARATH KURIAN 
#### Creation Date Thu 18 Feb 2021 04:12:05 AEDT
########################################
import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class Coin:
    def __init__(self,cName,cBuy,cSell,cTime):
        self.name =cName
        self.buy =cBuy
        self.sell=cSell
        self.time=cTime

    def getName(self):
        return self.name

    def getBuyValue(self):
        return self.buy

    def getSellValue(self):
        return self.sell

    def getTime(self):
        return self.time

    def setName(self,Name):
        self.name =Name

    def setBuyValue(self,bValue):
        self.buy =bValue
    
    def setSellValue(self,cValue):
        self.sell=cSell

    def printInfo(self):
        print(  "\nname:" + name
                +"\nbuy value"+buy
                +"\nsell value"+sell
                +"\n time"+time
             )   


class TradeList:
    def __init__(self):
        self.lock = threading.Lock()
        self.map=dict()
    
    def addtoList(self,coinObj):
        self.lock.acquire()
        try:
            #logging.debug('Acquired a lock')
            self.map[coinObj.getName()]=coinObj
        finally:
            #logging.debug('Released a lock')
            self.lock.release()

    def removeFrmList(self,name):
        self.lock.acquire()
        try:
            #logging.debug('Acquired a lock')
            self.map.pop(name,'None')
        finally:
            #logging.debug('Released a lock')
            self.lock.release()

            



