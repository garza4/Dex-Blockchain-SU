"""
Python has a Command Interpreter called argparse 
This can be used for the different interfaces


            (Wallet commands)
            WalletP: //when created, generates a random PrivateKey, takes a public key broadcast by nodes, encrypts the privatekey with the public key, sends it to the nodes to validate transactions 
	            Graph //contains the nodes of all transactions regarding the user. updated every transaction
	            PrivateKey //contains the private key used for hashing
	            Fee //records current fee. 
	            Balance //contains a double representing the total balance of a user for quick display. updated every transaction
	            TransactionHash(ammount. privatekey, address, timestamp, fee)// creates a new transaction hash for the transaction
	            TransactionBroadcast(amount, address, timestamp, hash, fee) //creates a node of the transaction, records it on the graph
	            		     				       //can be broadcast
	            Transfer(address, coinAmount) //checks amount is not negative, uses DFS on graph to find set of transactions that make it valid locally
	            			      //broadcasts transaction to local node or all nodes if valid, returning true. returns false if it fails for any reason
	            CreateToken(amount, decimals, symbol) //creates a new token by creating a node that records that amount, transferring a set coin amount to the 
	            				      //central bank address by sending it to a local node 
	            Exchange(symbol1, ammount1, symbol2, ammount2) //broadcasts to nodes, recorded on as a request for exchange. 
            WalletN:
            	Graph //contains the entire graph of all transactions recorded
            	Fee //contains the amount of coins as a fee for transactions 
            	TokenList //contains a list of all tokens symbols and digits, used for firing
            	KeyDict //a dictionary, containing all private keys of wallets, stored securely in some way (Still figuring out)
            	GetGraph() //calls central node or other nodes, requesting the graph to be sent. sets graph to be that received graph. 
            	SendGraph(address) //sends a graph to a given node address 
            	Validate(TransactionBroadcast(_,_,_,_,_), receivedAddress) //validates a transaction by checking the whole graph, using a DFS on the branch associated with the sender address
            									//checks all previous transactions concerning that address, stopping when some combination of past transactions is found that validates it
            	Listen(On/Off) //when on, will listen for transactions and validate them. when off the node does nothing. turning back on requires a get Graph. 
            	Exchange Handle (Exchange(_,_,_,_) //when a exchange is heard, will set it aside until a set of exchanges are found that fulfill the exchange. when one is found, creates a set of nodes on the graph that result in the same 
            					//thing as the exchange with one-way transactions via one receiver and one sender. Subdivides transactions if one can not be fully exchanged 
            	Update() //pings central node for Fee update, Fire update, and Freeze Update 
            	Fire(symbol) //will change all tokens sent using that symbol back into the native coin using the digits specified with the original creation 
            	Freeze(symbol) //will prevent any new transactions or exchanges using that symbol. 
            Central:
            	Graph //
                issueCoins(address, ammount): sends coins to a given adreess, provided it does not go over the total coin count. validated by private key signature
            	setFee(amount or %) will send out the updated fee to all nodes
            	setFire(symbol) broadcasts that a token is to be fired to all nodes
            	setFreeze(symbol) broadcasts that a token is to be frozen to all nodes 
            
                            