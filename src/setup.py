import hashlib as hlib
import network as net




class CentralBank:
    # CentralBank will keep track of information such as coin count, coin creation,
    # circulation, and totalCoins
    def __init__(self, coinInBank):
        # when a centralBank is called the "amount" of coins are made
        self.dictOfCoins = {}
        self.amountOfCoinType = {}            #this might have to be a dictionary of dictionaries so that at a position all the coins with unique ID numbers can be stored there. Like a probe
        self.coinInBank = coinInBank

    def createCoins(bank, amount, crypto):
        
        bank.coinInBank += amount
        bank.amountOfCoinType[crypto] = amount #amount of coins to create
        bank.dictOfCoins[crypto] = crypto
        print(bank.dictOfCoins[crypto])
    

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
    def __str__(self):
        return str(self.coinInBank)

class Node:
    # in order for the node class to work with networkx nodes have to be hashable
    # hash on uniqueID
    
    def __init__(self, amountExchanged, sender, receiver, timestamp, uniqueID, typeOfCoin):

        self.amountExchanged = amountExchanged
        self.receiver = receiver
        self.timestamp = timestamp
        self.uniqueID = uniqueID
        self.sender = sender
        self.typeOfCoin = typeOfCoin
    
    def __str__(self):
        return str(self.amountExchanged) + " " + self.sender.accountName + " " + self.receiver.accountName


class User:
    # in order to account for multiple coins a person can purchase, the amountOfCoin field will 
    # be a dict where keys are the coin names and at that position will be the amount that user has of that coin.
    def __init__(self, accountName, privateKey, publicKey):
        self.amountOfCoin = {} #a dictionary of coins and their amounts
        self.privateKey = privateKey #hash privateKey
        self.publicKey = publicKey
        self.transactions = [] # transactions will be a list of transactions...........
        self.accountName = accountName
        print("created user")

    def sendCoin(sender,receiver, amountToSend, typeOfCoin):
        if sender.amountOfCoin[typeOfCoin] > sender.amountOfCoin[typeOfCoin]:
            print ("Exceeded amount of coin to send")
            return False
        else:
            temp = sender.amountOfCoin[typeOfCoin]
            temp -= amountToSend
            sender.amountOfCoin[typeOfCoin] = temp
            return True

    def receiveCoin(receiver, receivingAmount, typeOfCoin):
        temp = receiver.amountOfCoin[typeOfCoin]
        temp += receivingAmount
        #print(receiver.amountOfCoin.keys())
        receiver.amountOfCoin[typeOfCoin] = temp
        return True
    
    def purchaseCoins(user, bank, amount, crypto):
        
        """
        when a purchase from the bank is made by a user, then -
            the user should gain the crypto they bought & lose the money they used to purchase the crypto
            the bank should lose the amount the person bought of that particular crypto
            
        need to find out if a user has a certain kind of coin, and still need to fix the key error.
            
        """
        
        temp = bank.amountOfCoinType[crypto] #typeOfCoin contains how much of that type of coin is stored in the bank, subtract from bank
        temp -= amount
        bank.amountOfCoinType[crypto] = temp
        bank.coinInBank -= amount
        if user.amountOfCoin[bank.dictOfCoins[crypto]] == 0:
            user.amountOfCoin[bank.dictOfCoins[crypto]] = amount
            
        else:
            tempAmount = user.amountOfCoin[crypto]
            tempAmount += amount
            user.amountOfCoin[crypto] = tempAmount
        #store how much of a coin a user has update that amount. Change the dictionary value to refelct the purchase
        #should also update amount of coin a user has after the purchase.....
    
    def __str__(self):
        return self.accountName + " has " + str(self.amountOfCoin)
    
    #^^^^^^^^^^^^be able to print a users transaction history; transactions is a list of nodes ^^^^^^^ 
       






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
