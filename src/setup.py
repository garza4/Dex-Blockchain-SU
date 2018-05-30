import hashlib as hlib
import network as net



class CentralBank:
    # CentralBank will keep track of information such as coin count, coin creation,
    # circulation, and totalCoins
    def __init__(self, freecoins, totalCoins, amount, typeOfCoin):
        # when a centralBank is called the "amount" of coins are made
        self.freecoins = freecoins
        self.totalCoins = totalCoins
        self.amount = amount
        self.coinDict = {}
        self.typeOfCoin = typeOfCoin

    def createCoins(amount, typeOfCoin):
        #coins will be a hash
        #have a function to create sequential coins
        bank = CentralBank(100000, 100000, amount, typeOfCoin)
        for i in range(0,bank.amount):
            bank.coinDict[i] = i % amount #this should be a hash for assigning unique values to coins 

    # def freezeCoins(self):
    #     #void a fishy transaction.
    #
    #
    # def deallocateCoins():
    #     #instead of burning send to an unreachable address that that only admin
    #     #can get to
    #
    # def trackFreeCoins():
    #     #keep track of coins that are currently not being used
    #     return self.freeCoins
    #
    # def makeTransaction(desiredAmount, ):
    #     #whenever someone buys a coin then subtract from freecoins

class Node:
    #in order for the node class to work with networkx nodes have to be hashable
    # hash on uniqueID
    def __init__(self, amountExchanged, sender, receiver, timestamp, uniqueID):

        self.amountExchanged = amountExchanged
        self.receiver = receiver
        self.timestamp = timestamp
        self.uniqueID = uniqueID
        self.sender = sender
    
    def __str__(self):
        return str(self.amountExchanged) + " " + self.sender.accountName + " " + self.receiver.accountName


class User:
    def __init__(self, accountName, amountOfCoin, privateKey, publicKey, transactions):
        self.amountOfCoin = amountOfCoin
        self.privateKey = privateKey #hash privateKey
        self.publicKey = publicKey
        self.transactions = [] # transactions will be a list of transactions...........
        self.accountName = accountName
        print("created user")

    def sendCoin(sender,receiver, amountToSend):
        if amountToSend > sender.amountOfCoin:
            print ("Exceeded amount of coin to send")
            return False
        else:
            sender.amountOfCoin -= amountToSend
            return True

    def receiveCoin(receiver, receivingAmount):
        receiver.amountOfCoin += receivingAmount
        return True
    
    def __str__(self):
        return self.accountName
       






class newToken():
    #could we call createCoins?
    #maybe a functional call, and then pass total supply and symbol?
    #central bank has to be able to handle new coins... new instance of central bank?
    def __init__(self, symbol, totalSupply, bank):
        self.symbol = symbol #allow for jpeg?
        self.totalSupply = totalSupply
        _self.bank = CentralBank() #have to check to make sure the syntax is correct, but this should be a private instance of the centralBank in newToken

    # def calculateCost():
    #
    # def buyCoin(symbol, coinNum):
