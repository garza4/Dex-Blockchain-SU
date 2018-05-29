import networkx as nx
import setup as setup

"""
Questions:
    Directed or undirected graph?
    Does the push and pop work for now?
    Can I save a pop call?

    Should the user have added and subtracted self.amount?
    For each transaction should there be a private instance of the user class or is passing setup.User ok since we supposedly know the sender and receiver

    ****************************************
    Random number generation for private keys - https://stackoverflow.com/questions/6088077/how-to-get-a-random-number-between-a-float-range?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    a good

    Used this to hash in scope project thing - https://en.wikipedia.org/wiki/Logistic_map
    
    going to need to write a function that can print nodes... shouldn't be too hard


"""

class Transaction:
#transactions are nodes so the graph will be made in the transaction class... I think...
    
     __lastTransaction = None
     #history is initialized to be 1000000 big all occupied with none
     __history = [None] * 1000000
     __G = nx.Graph()
     
     
    #create transaction will create a node for the two people included in the exchange.
    #adds a node to the graph and then adds an edge from the last transaction to the most current one.
     def createTransaction(sender, receiver, amount, transactionTime, uniqueID):
        #createTransaction is really like a createNode function since nodes are transactions
        # in main when createTransaction is called then have a function running passing in float64 numbers between 0 and 1
        
        __newTransaction = setup.Node(amount, sender, receiver, transactionTime, uniqueID) #private instance of the node class
        
        sender.sendCoin(sender, amount)
        receiver.receiveCoin(amount)
        sender.transactions.append(__newTransaction)                              #the transaction will be saved to the users account
        receiver.transactions.append(__newTransaction)                            #the transaction will be saved to the users account
        Transaction.__G.add_node(__newTransaction)
        lastEntry = Transaction.getLastTransaction()                                        #add one node for the sender (__newTransaction)
        Transaction.__G.add_edge(__newTransaction, lastEntry)                                 #workout a way to get the last node...
        Transaction.ledger(uniqueID, __newTransaction)
    
    #ledger will create a log of all transactions
     def ledger(uniqueID, transaction):
        """
        the ledger as of right now contains a hash that will store transactions with uniqueID's
        These ID's will be created using randomly generated numbersself. Users will have a history of their
        transactions, but this is not that history. the ledger class can be used to display information for the
        public to see.

        A little unsure what the uniqueID will end up being... a hash of the Users
        privateKey? (probably not the safest thing, but useful for us).

        Need a hash function here.
        """
        Transaction.__history[uniqueID] = transaction
        Transaction.__lastTransaction = Transaction.__history[uniqueID]
    
   #returns the last recorded transaction
     def getLastTransaction():
         return Transaction.__lastTransaction
    
    
    
