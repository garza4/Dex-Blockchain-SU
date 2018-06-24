import networkx as nx
import setup as setup
import hashlib as hlib


"""

    ****************************************
    Random number generation for private keys - https://stackoverflow.com/questions/6088077/how-to-get-a-random-number-between-a-float-range?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    a good
    Used this to hash in scope project thing - https://en.wikipedia.org/wiki/Logistic_map
    
    Also need to create a way to start splitting graphs in blocks. 
    
    python webserver information - https://docs.python.org/2/library/cgi.html
    
    python thread locks - https://docs.python.org/3/library/threading.html#lock-objects
    
   
"""

class Transaction:
    #The transaction class is where all nodes are going to be made (since nodes are transactions). 
    #createTransaction will be the method to call in order to create a newNode in the graph. 
    
     memPool = [nx.Graph()]
     memPoolSize = 10
     memPoolInc = 0
     block_keys = []
     
     def __init__(self, sender, receiever, amount, uniqueID, typeOfCoin, timestamp):
         self.sender = sender
         self.receiver = receiever
         self.amount = amount
         self.uniqueID = uniqueID
         self.typeOfCoin = typeOfCoin
     
    
    
     """
         createTransaction is really like a createNode function since nodes are transactions
         need to find out if the graph is empty before creating the first edge
         create transaction will create a node for the two people included in the exchange.
         adds a node to the graph and then adds an edge from the last transaction to the most current one.    
         
     """
     
     
     
     def createTransaction(sender, receiver, amount, transactionTime, uniqueID, typeOfCoin):
        
       # __newTransaction = setup.Node(amount, sender, receiver, transactionTime, uniqueID, typeOfCoin) #private instance of the node class
        __newTransaction = Transaction(sender,receiver, amount, transactionTime, uniqueID, typeOfCoin) 
        #print(__newTransaction)
        
        sender.sendCoin(receiver, amount, typeOfCoin)                         #the first parameter for sendCoin is taken care of by the sender var
        receiver.receiveCoin(amount, typeOfCoin)
        #here will be a check for fraud
        #if no fraud then append the transaction to sender and receiver
        
        sender.transactions.append(__newTransaction)                #the transaction will be saved to the users account
        receiver.transactions.append(__newTransaction)              #the transaction will be saved to the users account
        Transaction.memPool[Transaction.memPoolInc].add_node(__newTransaction)              #the last transaction is updated whenever a transaction is made by calling the ledger method. 
        lastEntry = Transaction.ledger(uniqueID, __newTransaction)  #add one node for the sender (__newTransaction)
        Transaction.memPool[Transaction.memPoolInc].add_edge(__newTransaction, lastEntry)        
        #in order to receive the latest transactions call ledger with uniqueID and a new transaction...
        #for example - last_transaction = ledger(uniqueID, new_transaction)    
        Transaction.blocks()
        
     # need a way to create different blocks and to distinguish where to start from in the mempool
     #Made a list of graphs and a counter
     def blocks():
         #will only create blocks when the specified size is reached
         #this function will create blocks, and it will be up to the forgers to validate all the transactions in the blocks we have...
         #which is TODO
         append_UIDS = ""
         listOfNodes = Transaction.memPool[Transaction.memPoolInc].nodes(data=False) # list of nodes get all the nodes in the mempool graph
         #Transaction.memPoolInc += 1
         for node in listOfNodes:
             key = append_UIDS + str(node.uniqueID)
             
         if len(Transaction.memPool[Transaction.memPoolInc]) >= Transaction.memPoolSize:
             
             if Transaction.memPoolInc > 0:
                 key = key + Transaction.memPool[Transaction.memPoolInc - 1]
                 Transaction.block_keys.append((Transaction.memPoolInc , hlib.sha256(key)))     
                 Transaction.memPoolInc += 1 
                 Transaction.memPool[Transaction.memPoolInc].append(nx.graph())
             else: #firstBlock
                 key = append_UIDS + key
                 Transaction.block_keys.append((Transaction.memPoolInc , hlib.sha256(key)))
                 Transaction.memPoolInc += 1 
         
                   
        
     
     """
        the memPool can be the graph G. 
        We will have a function that goes through G and verifies transactions and once a transaction has been verified it will be added to the 
        actual graph. 
        The function will take a graph and verify nodes which are transactions
        Found a way that could make this process easy - https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.Graph.nodes.html
        .data returns an nlist of nodes which we can then use to verify transactions. 
        
    
        Need to start thinking about threadSafe code so that if our code is running on the cloud nothing gets messed up
        Research Locks and such for python
        """
     
     def __str__(self):
         return str(self.sender) + " " + str(self.uniqueID) 
         #str(self.sender) + " " + str(self.receiver) + " " + str(self.uniqueID)   
         
     def __repr__(self):
         return str(self)
    
    
    
     #call when we want to the validate the mempool
     #THIS METHOD NEEDS WORK
     def __validateTransactions():
         listOfNodes = Transaction.memPool[Transaction.memPoolInc].nodes(data=False) # list of nodes get all the nodes in the mempool graph
         size_of_graph = len(Transaction.memPool[Transaction.memPoolInc])
         #reversed will start iterating from the last added node
         for nodes in reversed(listOfNodes):
               size_of_graph -= 1
               #I have no idea why the uniqueID's are all 1529115084.2049956....
               #print(nodes.uniqueID)
               m_tree = hlib.sha256()
               m_tree.update(str(nodes.uniqueID))
             
    
    
     #ledger will create a log of all transactions
     __lastTransaction = None
     __history = [None] * 1000000 #history is initialized to be 1000000 big all occupied with none
     
     def ledger(uniqueID, transaction):
        """
        the ledger as of right now contains a hash that will store transactions with uniqueID's
        These ID's will be created using randomly generated numbers. Users will have a history of their
        transactions, but this is not that history. the ledger class can be used to display information for the
        public to see.
        A little unsure what the uniqueID will end up being... a hash of the Users
        privateKey? (probably not the safest thing, but useful for us).
        Need a hash function here.
        """
        Transaction.__history[uniqueID] = transaction
        Transaction.__lastTransaction = Transaction.__history[uniqueID]
        #print(transaction) #which is a node
        return Transaction.__lastTransaction
    
    
         #returns the last recorded transaction
     def getLastTransaction():
         return Transaction.__lastTransaction
     
     
         
"""   
class Token(Transaction):
    
    def createToken(amount, tokenID, decimalValue):
        Transaction.createTransaction(sender, CentralBankAddress, (amount*decimalValue),transactionTime, uniqueID, tokenID)
        __newToken = setup.Node(amount, sender, tokenID)
        sender.reciveCoint(amount,tokenID)
        sender.transactions.append(__newTransaction)                #the transaction will be saved to the users account
        Transaction.G.add_node(__newTransaction)                    #the last transaction is updated whenever a transaction is made by calling the ledger method. 
        lastEntry = Transaction.getLastTransaction()                #add one node for the sender (__newTransaction)
        Transaction.G.add_edge(__newTransaction, lastEntry)        
        Transaction.ledger(uniqueID, __newTransaction)
    
    #def burnToken(tokenID):
    
    #def freezeToken(tokenID):
"""