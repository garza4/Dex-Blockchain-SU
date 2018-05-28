import networkx as nx
from src.setup import * as setup

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


"""

class Transaction:
#transactions are nodes so the graph will be made in the transaction class... I think...

    __G = nx.Graph()
    __idHolder = {}
    __transactionCounter = 0

    def createTransaction(sender, receiver, amount, transactionTime, uniqueID):
        #createTransaction is really like a createNode function since nodes are transactions
        # in main when createTransaction is called then have a function running passing in float64 numbers between 0 and 1

        __newTransaction = setup.Node(amount, sender, receiver, transactionTime) #private instance of the node class

        setup.User.sendCoin(sender, amount)
        setup.User.receiveCoin(receiver, amount)
        G.add_node(__newTransaction)                                            #add one node for the sender (__newTransaction)
        G.add_edge(__newTransaction, setup.Node.previous)                       #workout a way to get the last node... 
        ledger(uniqueID, __newTransaction)
        __transactionCounter++                                                  #this will create a topographic graph, but is this what we want? Undirected

    def ledger(uniqueID, transaction):
        history = {}
        history[uniqueID] = transaction
        #uniqueID's are going to be generated with a call...
