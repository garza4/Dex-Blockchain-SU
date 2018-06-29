# -*- coding: utf-8 -*-

""" TO DO
* weight random forger selection DONE -- used random.choices method and replaced duplicates with new users
* method to give transaction fees to chosen forger
* method to check waiting stake holders and release funds as they become eligible

* provide a suggested aglorithm to validate transactions
"""

""" Questions
* should we allow stake holders to add to their stake without resetting their start date and time?
"""   
import datetime
import random
import setup 

class Stake():
    #Stake class will keep track of the current users who have stake for forging
    #and the users who have decided to pull their stake, but have not had their
    #money relased to them
    def __init__(self, validated_job):
        self.__stakeHolders = {} #{userID: [amount of stake, date and time stake was added]}
        self.__waitingStake = {} #{userID: [amount of stake, date and time of stake removal]}
        self.earnings = []       # when a forger has validated a transaction - forger.append(award)
        self.validated_job = False# this can be used to determine o
        
    #Returns whether the given user is in the __stakeHolders dictionary or not
    def __isInDictionary(self, userID):
        for key in self.__stakeHolders:
            if key == userID: #userID was found, return true and end function
                return True
        return False #userID was never found, so return false
        
    #Adds the userID, amount of stake, and date/time to the dictionary of __stakeHolders
    def addStake(self, userID, amount):
        self.__stakeHolders[userID] = [amount, datetime.datetime.now() - datetime.timedelta(days=31)]
    
    #Removes the userID form __stakeHolder and adds ID and amount to _waitingStake if user currently holds stake
    #This is used in the blocksToValidate method
    def removeStake(self, userID, forgerEarnings): 
        if self.__isInDictionary(userID):
            totalAmount = self.__stakeHolders[userID][0] + forgerEarnings
            self.__waitingStake[userID] = [totalAmount, datetime.datetime.now()]
            print (self.__waitingStake)
            del self.__stakeHolders[userID]
        else:
            print ('User ', userID, ' is not a stake holder')
            
    #used if stakeholder decides to remove their money from the pool before they become a forger
    def removeStakeWithoutReward(self, userID):
        if self.__isInDictionary(userID):
            setup.User.receiveCoin(userID, self.__stakeHolders[userID][0], "bnb")
            del self.__stakeHolders[userID]
        else:
            print ('User ', userID, ' is not a stake holder')
    
    #Returns the amount of stake for the given user if user is currently a stake holder
    def getStakeAmount(self, userID):
        if self.__isInDictionary(userID):
            return self.__stakeHolders[userID][0]
        else:
            return 'User ', userID, ' is not a stake holder'
    
    #Chooses a set of x users to be the forgers for the transactions that need to be added to the graph
    #The user at index 0 of the list will be the chosen forger and indicies 1 to x-1 will be backup forgers
    def chooseStakeHolders(self, x):
        potentialForgers = [] #userIDs of stake holders who have held stake for more than 30 days
        forgerWeights = [] #coinAge for users in potentialForgers array (parallel arrays)
        currentTime = datetime.datetime.now() #time and date that we start picking forgers
        totalCoinAge = 0
        
        #for each of the stake holders, if they have held stake for more than 29 days,
        #add their userID and coinAge to the parallel arrays
        for key in self.__stakeHolders:
            daysInStake = currentTime - self.__stakeHolders[key][1]
            if daysInStake.days >= 30:
                totalDays = daysInStake.days
                if totalDays > 90: #no more benefit day wise if stake held for more than 90 days
                    totalDays = 90
                coinAge = self.__stakeHolders[key][0] * totalDays
                totalCoinAge += coinAge
                potentialForgers.append(key)
                forgerWeights.append(coinAge)

        forgers = random.choices(population=potentialForgers, weights=forgerWeights, cum_weights=None,  k=x) #.choices() takes into account forger's coinAge but replaces after chosing
        
        #remove duplicate forger IDs from the list
        #I didn't make this a private method because we need to have access to the potentialForgers and forgerWeights arrays
        uniqueForgers = []
        for x in forgers:
            if x in uniqueForgers:
                #find new stake holder
                newForger = random.choices(population=potentialForgers, weights=forgerWeights, cum_weights=None,  k=1)
                while newForger[0] in uniqueForgers:
                    newForger = random.choices(population=potentialForgers, weights=forgerWeights, cum_weights=None,  k=1)
                uniqueForgers.append(newForger[0])
            else:
                uniqueForgers.append(x)

        return uniqueForgers
    
class main():
    """ FOR TESTING
    stakeholders = Stake()
    stakeholders.addStake(1234, 300.00)
    stakeholders.addStake(5678, 9000.00)
    stakeholders.addStake(9123, 40000.00)
    #print(stakeholders.getStakeAmount(1234))
    #print(stakeholders.getStakeAmount(5678))
    list = stakeholders.chooseStakeHolders(2)
    print(list)
    
    #stakeholders.removeStake(1235)
    #print (stakeholders.getStakeAmount(1234))
     """
    
    
main()
                