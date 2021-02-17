#########################################
#### File Name : Event.py 
#### Path : . 
#### Author SHARATH KURIAN 
#### Creation Date Wed 17 Feb 2021 05:51:50 AEDT
########################################
from enum import Enum
class Event:
    
    

        def __init__(self,tId,tValue,tOpCode,tAction,tCoin):
            self.coin =tCoin
            self.id    =tId 
            self.status ="OPEN"  # OPEN CANCEL CLOSE PAUSE
            self.cValue=tValue   # NUMERICAL VALUE
            self.action=tAction  # BUY/SELL/ALERT
            self.opCode=tOpCode  # 0 LESS 1 MORE
            self.oEvents = list()

        def getCoin(self):
            return self.coin

        def setCoin(self,tCoin):
            self.coin=tCoin

        def getId(self):
            return self.id
        def setId(self,tId):
            self.id=tId

        def getStatus(self):
            return self.status

        def setStatus(self,tStatus):
            self.sttaus = tStatus 

        def getValue(self):
            return self.cValue

        def setValue(self,tValue):
            self.cValue = tValue

        def getAction(self):
            return self.action

        def setAction(self,tAction):
            self.action = tAction

        def getOpCode(self):
            return self.opCode
        def setOpCode(self,tOpCode):
            self.opCode = tOpCode


        def getEvents(self):
            return self.oEvents
        def setEvents(self,nList):
            self.oEvents = nList
        def addEvents(self,nId):
            self.oEvents.append(nId)



        def printInfo(self):

            print("\n Coin : "+self.coin 
                    +"\n ID :"+self.id
                    +"\n Status :"+self.status
                    +"\n Value :"+str(self.cValue)
                    +"\n Action :"+str(self.action)
                    +"\n OpCode :"+str(self.opCode)
                    +"\n Related Events :"+str(self.oEvents)
                )


Status = Enum('Status','OPEN CLOSED CANCEL PAUSE')
Action = Enum('Action','BUY SELL ALERT')
            
obj =  Event("t1",123,0,"BUY","XRP")
obj.printInfo()
