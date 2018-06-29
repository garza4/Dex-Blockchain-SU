import networkx as nx
import setup as setup
import hashlib as hlib

import datetime


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
     
     def __init__(self, sender, receiever, amount, uniqueID, typeOfCoin, timestamp, srcTransactionID):
         self.sender = sender
         self.receiver = receiever
         self.amount = amount
         self.uniqueID = uniqueID
         self.typeOfCoin = typeOfCoin
         self.timeStamp = timestamp
         self.sourceOfCoin = srcTransactionID   #the unique ID of the transaction from where the sender received the money they want to send
     
    
    
     """
         createTransaction is really like a createNode function since nodes are transactions
         need to find out if the graph is empty before creating the first edge
         create transaction will create a node for the two people included in the exchange.
         adds a node to the graph and then adds an edge from the last transaction to the most current one.    
         
     """
     
     
     
     def createTransaction(sender, receiver, amount, transactionTime, uniqueID, typeOfCoin, srcTransactionID):
        
       # __newTransaction = setup.Node(amount, sender, receiver, transactionTime, uniqueID, typeOfCoin) #private instance of the node class
        __newTransaction = Transaction(sender,receiver, amount, transactionTime, uniqueID, typeOfCoin, srcTransactionID) 
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
        Transaction.blocks()
        
        
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
    
    #assigns the blocks from the previous day for forger to validate
     def __blocksToValidate():
        currTime = datetime.datetime.now()
        index = 0 #should always check mempool at index 0 because __validateTransaction will delete 
        #the block that was validated making the next block to be validated at index 0
        transactionTime = Transaction.memPool[index].timeStamp
        while (currTime-transactionTime).days >= 0:
            if (currTime-transactionTime).minutes > 0:
                nx.Transaction.__validateTransactions()
                transactionTime = Transaction.memPool[index].timeStamp
        
    
     #call when we want to the validate one block in the mempool
     #THIS METHOD NEEDS WORK
     def __validateTransactions():
         #Note: I think the index we want to use is 0 not Transaction.memPoolInc becuase we want the earliest created block to be valiedated first
         #if the mempool is not set up like a queue, please change back to the way it was
         listOfNodes = Transaction.memPool[0].nodes(data=False) # list of nodes get all the nodes in the mempool graph at the earliest created block
         size_of_graph = len(Transaction.memPool[0])
         graphOfValidTransactions = nx.Graph
         lastNode = None
         #reversed will start iterating from the last added node
         for nodes in reversed(listOfNodes):
               size_of_graph -= 1
               #I have no idea why the uniqueID's are all 1529115084.2049956....
               #print(nodes.uniqueID)
               
               #look at the reference transaction for the amount given to sender
               srcForSender = nodes.sourceOfCoin #unique of ID of the transaction the sender claims they received the money from
               srcTransaction = Transaction.__history[srcForSender]
               
               #We will assume that the coin type must be the same between the two transactions
               if nodes.typeOfCoin == srcTransaction.typeOfCoin:
                   #there is enough money to transfer
                   #though this doesn't take into account if the sender has already referenced this transaction
                   if srcTransaction.amount >= nodes.amount: 
                       #add it to the graph for the new block
                       graphOfValidTransactions.add_node(nodes)
                       graphOfValidTransactions.add_edge(nodes, lastNode)
                       lastNode = nodes
                       
                       #complete transaction by adding amount to receiver account and removing amount from sender account
                       setup.User.sendCoin(nodes.sender,nodes.receiver, nodes.amount, nodes.typeOfCoin)
                       setup.User.receiveCoin(nodes.receiver, nodes.amount, nodes.typeOfCoin)
                        
        #add new block to the official graph/blockchain?
         setup.CentralBank.blockChain.addBlock(graphOfValidTransactions)
        
        #remove the first block from the mempool
         Transaction.memPool.pop(0)  
               
        #is this for a merkle tree?
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
     
     
class Block():
    def __init__(self, graph, currHash, prevHash, timestamp):
        self.hashOfBlock = currHash
        self.hashOfPrevBlock = prevHash
        self.Graph = graph
        self.time = timestamp
        
    def getGraph(self):
        return self.Graph
    
    def getHash(self):
        return self.hashOfBlock
    
    def getPrevHash(self):
        return self.hashOfPrevBlock
    
    def getTimeStamp(self):
        return self.time
        
class BlockChain():
    def __init__(self):
        self.blockHashes = []
        
    def addBlock(self, graph):
        currHash = 0
        graphHash = hlib.sha256(graph)
        currDate = datetime.datetime.now()
        currDateHash = hlib.sha256(currDate)
        
        if len(self.blockHashes) == 0: #this is the first block in the chain
            currHash = hlib.sha256(graphHash + currDateHash + hlib.sha256(0),currDate)
            Block(graph, currHash, 0)
        else: #there is at least one other block in the chain
            currHash = hlib.sha256(graphHash + currDateHash + hlib.sha256(self.blockHashes[-1]))
            Block(graph, currHash, self.blockHashes[-1],currDate)
            
        self.blockHashes.append(currHash)
        
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