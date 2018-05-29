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


"""

class Transaction:
#transactions are nodes so the graph will be made in the transaction class... I think...

    __G = nx.Graph()


    def createTransaction(sender, receiver, amount, transactionTime, uniqueID):
        #createTransaction is really like a createNode function since nodes are transactions
        # in main when createTransaction is called then have a function running passing in float64 numbers between 0 and 1

        __newTransaction = setup.Node(amount, sender, receiver, transactionTime, uniqueID) #private instance of the node class

        sender.sendCoin(sender, amount)
        receiver.receiveCoin(receiver, amount)
        sender.transactions.push(__newTransaction)                              #the transaction will be saved to the users account
        receiver.transactions.push(__newTransaction)                            #the transaction will be saved to the users account
        G.add_node(__newTransaction)
        lastEntry = getLastTransaction()                                        #add one node for the sender (__newTransaction)
        G.add_edge(__newTransaction, lastEntry)                                 #workout a way to get the last node...
        ledger(uniqueID, __newTransaction)

    __lastTransaction = None
    __history = {}
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

        history[uniqueID] = transaction
        __lastTransaction = history[uniqueID]

    def getLastTransaction():
        return __lastTransaction
