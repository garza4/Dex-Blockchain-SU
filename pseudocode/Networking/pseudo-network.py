# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:01:53 2018

@author: rjg24_000
"""

"""
references 
****************************************

1) https://softwareengineering.stackexchange.com/questions/187403/import-module-vs-from-module-import-function how to import stuff... 
2) https://docs.python.org/3/tutorial/classes.html -python classes private and more
3) https://stellar-base.readthedocs.io/en/latest/api.html#api -stellar base api
4) https://stackoverflow.com/questions/8212053/private-constructor-in-python - public and private for python 
5) https://www.geeksforgeeks.org/private-variables-python/ - private variables in python
6) https://stackoverflow.com/questions/15281746/custom-data-structures-in-python - for custom data structures i.e. coins and such... 

from stellar_base.memo include Memo --- how to include stellar libraries

****************************************

Networking - 
    
    class CentralBank:
        
        CentralBank is made into a constructor with the def __init__ call, which can be found at link 6. 
        
        def __init__(self, freeCoins, totalCoins, anything else???):
                
            def createCoins(self):
                call a function to create coins
        
            def freezeCoins(self):
                call if there is suspicious activity happening, 
                with the graph implementation I think this method will be called if we see overspending
                to make an instance of freezeCoins for the graph do this -- freeze = _freezeCoins
            
            
            def deallocateCoins(self):
                instead of "burning" we will send coins to an address that no one else can get to except the bank
                call sendCoins(address) method, i think we will have an address to send coins that will be deallocated...
                also to keep track of what addresses (coins) are valid we will need to have a data structure that can keep track of valid coins and coins that have been taken
                    ...maybe a dictionary. Hash here??? ask Sara
            
            
            def checkCirculation(self):
                return self.freeCoins
                when coins are initially created we can just pass pass a designated amount of free coins no matter what... 
                
    class graph:
        def __init__ (self, nodes,...anything else?):
            
            def sendCoin(amount, toWho):
        
            def makePurchase(amount, toWho):
                the toWho will be the username of the person trying to get the coin... We will have that information from the Master Dictionary
            
            def checkForValidTransaction(user, transaction):
                this function will be the continuous checking that ensures that all transactions up to that transaction have been valid, if it is not valid then return false and void
                the fraudulent transaction. 
                
            
        
        
"""
    