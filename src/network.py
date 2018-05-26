import networkx as nx
from src.setup import * as setup

"""
Questions:
    Directed or undirected graph?
    Does the push and pop work for now?
    Can I save a pop call?

    Should the user have added and subtracted self.amount?
    For each transaction should there be a private instance of the user class or is passing setup.User ok since we supposedly know the sender and receiver




"""

class Transaction:
#transactions are nodes so the graph will be made in the transaction class... I think...
#i don't think the transaction constructor needs a sender attribute since you know yourself...
    __G = nx.Graph()
    nodeDict = {}
    def __init__(self, sender, receiver, amount, transactionTime, previousTransaction):

        self.receiver = setup.User.publicKey
        self.amount = amount
        self.transactionTime = transactionTime
        self.previousTransaction = setup.Node.nodePop()


    def createTransaction(sender, receiver, amount): #createTransaction is really like createNode

        __newTransaction = setup.Node(self, self.amount, self.sender, self.receiver, self.transactionTime) #private instance of the node class

        setup.User.sendCoin(sender, self.amount)
        setup.User.receiveCoin(receiver, self.amount)
        G.add_node(__newTransaction)                                            #add one node for the sender (__newTransaction)
        G.add_edge(__newTransaction, self.previousTransaction)                  #this will create a topographic graph, but is this what we want? Undirected
        setup.Node.nodePush(__newTransaction)                                   #the latest node is now the previous transaction

    def ledger():
        
