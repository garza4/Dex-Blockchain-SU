# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:01:53 2018

@author: rjg24_000
"""

"""
references 
****************************************
From 5/14/18
1) https://softwareengineering.stackexchange.com/questions/187403/import-module-vs-from-module-import-function how to import stuff... 
2) https://docs.python.org/3/tutorial/classes.html -python classes private and more
3) https://stellar-base.readthedocs.io/en/latest/api.html#api -stellar base api
4) https://stackoverflow.com/questions/8212053/private-constructor-in-python - public and private for python 
5) https://www.geeksforgeeks.org/private-variables-python/ - private variables in python
6) https://stackoverflow.com/questions/15281746/custom-data-structures-in-python - for custom data structures i.e. coins and such... 

From 5/15/18
7) https://www.youtube.com/watch?v=0v9ATbJTQDc - this is a pretty good video explaining how to call different objects from different classes, it's only five minutes, worth a watch. 
8) https://networkx.github.io/documentation/stable/install.html - found the standard python library for graphs... We might not actually need to use stellar-base... We'll see
9) https://neonx.readthedocs.io/en/latest/readme.html - Emailed Dr. Stolper asking for a graph reccommendation, gave networkX. Also reccommended neo4j for node database

from stellar_base.memo include Memo --- how to include stellar libraries -- lol might not need

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
                
    class node: //should be hashable... store in dictionary? or array?  
        each node will hold sender data, transaction, private sender key,timestamp and the recipiant all hashed
        
        

        "If you have a data structure already in place to describe nodes you can simply use that structure as your nodes provided it is hashable."
        NetworkX is the standard python graph library, so if we make a node class with everything we want (as long the nodes are hashable) then creating the graph with networkX should be 
        pretty simple... 
        
        
        def __init__ (self, user, transactionInfo):
            
            def createNode(self, sender, receiver, amount):
                Nodes are transactions so this should create a new node node linking two users. 
                user.amountOfCoin = user.amountOfCoin - amount
                if(checkForValidTransaction(user, amount)) then self.add(newNode)
                
            
        
            def makePurchase(amount, toWho):
                the "toWho" will be the username of the person trying to get the coin... We will have that information from the Master Dictionary
            
            def checkForValidTransaction(user, amountOfCoin):
                this function will be the continuous checking that ensures that all transactions up to that transaction have been valid, if it is not valid then return false and void
                the fraudulent transaction. 
                
    class user:
            def __init__(self, amountOfCoin, privateKey):
                def createUser(key):
                    hash(key) - the hash function creates a unique hash value for a user. 
                    
                
   class minter:
            def GetGraph(); // gets all new transactions to add to graph, initially this will be the whole graph
                            //adds nodes to the graph by timestamp, validating each transaction it hears          
        
    class newToken:
        def createToken(symbol, supply, miningDec)

        "Native support for new token generation is required. That is, users should be able to create new tokens simply by specifying token parameters, such as symbol, total supply, decimals, etc, without having to write smart contracts. New token generation will cost a fee, payable in the native coin of the blockchain.
        Tokens can follow a simple structure; fixed supply, all pre-mined, etc. Again, if there is a need for a trade-off between advanced features vs speed and simplicity, the latter wins"

        def calculateCost():
            //finds the fee that must be paid by the new token creator, using total supply of the new token and current supply of the native coin
        
        def buyCoin(symbol, coinNum):
            // when called, a user buys the ammount of tokens based on the ammount of coins spent. This must also check total supply or there must be some way to calculate the ammount of tokens left in the system
             
        //calls a new node to create this new token, using the Dec to determine value of the coin. 

"""
    