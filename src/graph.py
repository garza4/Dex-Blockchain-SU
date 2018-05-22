import networkx as nx



class CentralBank:
    # CentralBank will keep track of information such as coin count, coin creation,
    # circulation, and totalCoins
    def __init__(self, freecoins, totalCoins):
        self.freecoins = freecoins
        self.totalCoins = totalCoins


        def createCoins(self):
            #coins will be a hash
            #have a function to create sequential coins


        def freezeCoins(self):
            #void a fishy transaction.


        def deallocateCoins():
            #instead of burning send to an unreachable address that that only admin
            #can get to

        def trackFreeCoins():
            #keep track of coins that are currently not being used

        def makeTransaction(desiredAmount, ):
            #whenever someone buys a coin then subtract from freecoins

class Node:
    #in order for the node class to work with networkx nodes have to be hashable

    def __init__(self, user, amountExchanged, receiver, timestamp):
        self.user = user
        self.amountExchanged = amountExchanged
        self.receiver = receiver
        self.timestamp = timestamp

class User:
    def __init__(self, amountOfCoin, privateKey):
        self.amountOfCoin = amountOfCoin
        self.privateKey = privateKey #hash privateKey

        def createUser(key):
            #call a hash to make a user

class Minter:

    def CheckForValidTransaction(user, amountExchanged):


    def getGraph():



class newToken():
    #could we call createCoins?
    #maybe a functional call, and then pass total supply and symbol?
    #central bank has to be able to handle new coins... new instance of central bank?
    def __init__(self, symbol, totalSupply, bank):
        self.symbol = symbol #allow for jpeg?
        self.totalSupply = totalSupply
        _self.bank = CentralBank() #have to check to make sure the syntax is correct, but this should be a private instance of the centralBank in newToken

        def calculateCost():

        def buyCoin(symbol, coinNum):
