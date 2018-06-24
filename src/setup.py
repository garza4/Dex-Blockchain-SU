import hashlib as hlib
import network as net
import ConsensusAlgorithm as cA
import datetime





class CentralBank:
    # CentralBank will keep track of information such as coin count, coin creation,
    # circulation, and totalCoins
    is_running = False
    def __init__(self, coinInBank):
        # when a centralBank is called the "amount" of coins are made
        self.dictOfCoins = {}
        self.amountOfCoinType = {}            #this might have to be a dictionary of dictionaries so that at a position all the coins with unique ID numbers can be stored there. Like a probe
        self.coinInBank = coinInBank
        self.listOfUsers = []                 #uniqueID's
        #need to be able to get a user from knowing their uniqueID
    def createCoins(bank, amount, crypto):
        bank.coinInBank += amount
        bank.amountOfCoinType[crypto] = amount #amount of coins to create
        bank.dictOfCoins[crypto] = crypto
        #is_running = True
    
    """
    at the start of the day (if the class is called) pick forgers 
    """
    while is_running:
        #need to figure out how to start looking for forgers using time
        start_of_day = datetime.datetime(8, 0, 0, 0) #8:00:00:00 AM
        currTime = datetime.datetime.now()
        
        if (currTime.hour - start_of_day.hour) == 0: #The current time is between 8 and 9 am
            if (currTime.minute - start_of_day.minute) == 0: # The current time is between 8 and 8:01 am
                if (currTime.second - start_of_day.second) == 0: #The current time is between 8 and 8:00:01 am
                    list_of_holders = cA.chooseStakeHolders(20)
                    prime_stake = list_of_holders[0] 
                    #primeStake will be a privateKey for that user
                    """
                    The value for 'holders' can either be userID or user's private key depending on which unique value
                    we pass to the addStake method in ConsensusAlgorithm.py
                    As of now, it is userID. 
                    Maybe we can send the message based on userID?
                    
                    for holders in list_of_holders:
                        user = getUser(holders_privateKey) # returns user instance
                        user.alerts.append("you have been chosen as a stake holder")
                        #find a way to display if they are a forger.                         
                        #One forger, but notify all that were chosen.
                        
                        
                    ******** to show this we can open windows for all those users... In our case if there were 12 candidates then 
                                12 windows would open with a message and maybe the users name as the title of the window. 
                    """

        # Continuously checks for forgers who have waited 30 to have their stake released
        # Warning: I have not tested this loop and
        #__waitingStake needs the name of an instance of the Stake class that I think was initialized in another file
        for successfulForger in cA.Stake.__waitingStake:
            timeStakeAdded = __waitingStake[successfulForger][1]
            if (currTime - timeStakeAdded) >= 30:
                #either make a new transaction to give forger their money back
                #or directly add amount to account, but then there would be no record of it in the graph
                del __waitingStake[successfulForger]
                
        
        """
        What we coded together
        plus_one = datetime.datetime(8, 0, 59, 0)
        delta = plus_one - start_of_day
        
        if datetime.time() == 
            list_of_holders = cA.chooseStakeHolders(20):
            prime_stake = list_of_holders[0] 
            primeStake will be a privateKey for that user
                for holders in list_of_holders:
                    user = getUser(holders_privateKey) - returns user instance
                    user.alerts.append("you have been chosen as a stake holder")
                    #find a way to display if they are a forger. 
                    
                    One forger, but notify all that were chosen. 
        """
        
    # def freezeCoins(self):
    #     #void a fishy transaction.
    #
    #
    # def deallocateCoins():
    #     #instead of burning send to an unreachable address that that only admin
    #     #can get to
    #
  
    def __str__(self):
        return str(self.coinInBank)


class User:
    # in order to account for multiple coins a person can purchase, the amountOfCoin field will 
    # be a dict where keys are the coin names and at that position will be the amount that user has of that coin.
    def __init__(self, accountName, privateKey):
        #removed publicKey because it was weird to work with in network
        self.amountOfCoin = {} #a dictionary of coins and their amounts
        self.privateKey = privateKey #hash privateKey
        #self.publicKey = publicKey
        self.transactions = [] # transactions will be a list of transactions...........
        self.accountName = accountName
        self.alerts = []
        #print("created user")
        
        
    #don't call except when validating memPool...     
    def __getUniqueID(user):
        return user.privateKey

    def sendCoin(sender,receiver, amountToSend, typeOfCoin):
        if amountToSend > sender.amountOfCoin[typeOfCoin]:
            print ("Exceeded amount of coin to send")
            return False
        else:
            temp = sender.amountOfCoin[typeOfCoin]
            temp -= amountToSend
            sender.amountOfCoin[typeOfCoin] = temp
            return True

    def receiveCoin(receiver, receivingAmount, typeOfCoin):
        if typeOfCoin not in receiver.amountOfCoin.keys():
            receiver.amountOfCoin[typeOfCoin] = receivingAmount
            return True
        
        else:    
            temp = receiver.amountOfCoin[typeOfCoin]
            temp += receivingAmount
            receiver.amountOfCoin[typeOfCoin] = temp
            return True
        print("is this spot always reached?")
        return False
    
    #the only acceptable coin for stake is bnb
    def put_up_stake(self,ID, amount):
        if self.amountOfCoin["bnb"] < amount:
                return False
        else:
            cA.Stake.addStake(ID, amount) #might need self
            self.amountOfCoin["bnb"] -= amount #prevents user from spending money they have put up as stake
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
        #print("the amount of coin is " +  " " + str(temp))
        bank.amountOfCoinType[crypto] = temp
        #print("the bank now has " + str(bank.amountOfCoinType[crypto]) + " " + "coin in the bank")
        bank.coinInBank -= amount
        #print("I am trying to purchase " + crypto)
        #print(user.amountOfCoin.keys())
        if not user.amountOfCoin.keys():
            user.amountOfCoin[crypto] = 0
        #print(user.amountOfCoin.keys())
    
        if user.amountOfCoin[crypto] == 0:
            user.amountOfCoin[crypto] = amount
            #print(str(user.amountOfCoin[crypto]) + " users purchase" )
            
        else:
            tempAmount = user.amountOfCoin[crypto]
            tempAmount += amount
            user.amountOfCoin[crypto] = tempAmount
        #store how much of a coin a user has update that amount. Change the dictionary value to refelct the purchase
        #should also update amount of coin a user has after the purchase.....
    
    def __str__(self):
        return self.accountName + " has " + str(self.amountOfCoin)
    
    #^^^^^^^^^^^^be able to print a users transaction history; transactions is a list of nodes ^^^^^^^ 
       
    
    #with this method there will also have to be a check  alerts method of somesort.
    def sendMessage(user, message):
        user.alerts = message
        





class newToken():
    _cost = None
    #could we call createCoins?
    #maybe a functional call, and then pass total supply and symbol?
    #central bank has to be able to handle new coins... new instance of central bank?
    def __init__(self, symbol, totalSupply, bank, decimalValue):
        self.symbol = symbol #allow for jpeg?
        self.totalSupply = totalSupply
        self.bank = CentralBank() #have to check to make sure the syntax is correct, but this should be a private instance of the centralBank in newToken
                                    #why not just make a dict of newTokens that has the supply and symbol instead of a new centralBank instance for each token?
        self.value=decimalValue

    def calculateCost(totalSupply, decimalValue):
       _cost= (totalSupply * decimalValue) #cost is calculated by the user defined value for the token compared to Binance Coin multiplied by the total amount, removing that amount of Binance coin and replacing it with the new token
    # def buyCoin(symbol, coinNum): No buying coins, we can just swap them on the decentralized Exchange when implemented, letting the users define the cost of a coin
