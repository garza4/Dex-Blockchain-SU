"""
Python has a Command Interpreter called argparse 
This can be used for the different interfaces

Personal Wallet Interface (Hold Y ammount of transactions for a single user): 
    Commands: 
            Send(double x, recipiant address): Sends x ammount of the native coin to the address specified 
                                               by broadcasting this transaction to network nodes that contain 
                                                and validate all transactions. Returns true if sucsessful, false
                                                if not. Will also return false if the ammount sent is more than currently 
                                                held by the wallet. Takes the transaction, recipiant, walletAddress, timestamp, and private key, sending the hash. The
                                                network node then validates it by checking the hash and using the consensus alg, seeing that a transaciton is valid by
                                                checking the previous transactions of the sender. 
            Receive(): A function constantly pinging local network nodes to find any transactions involving the wallent, 
                                                specifically if any coins have been sent to the wallet 
            CreateToken(Symb, amm, digets, etc): Sends a transaction to a node, creating a new token and burning the required ammount of coins for it
                                                Returns true if created, false if one token already exists with the same symbol
            Exchange(SymbA, SymbB): Echanges tokens for tokens or tokens for coins or vice versa by broadcasting the request to a local network node, 
                                    Returns true if the exchange occurs and updates wallet, false if no exchange is possable or does not occur, the token is
                                    fired, or the token does not exist
Network Nodes (Hold copies of the entire network )
            Validate(transaction): Takes a transaction and validates it by checking the sender's branch of the graph, finding a valid set of transactions that
                                    allow it to be possable. Also factors in expense for sending the coins/tokens
            Listen(): A function that continuously listens for transactions and getGraphs().
            getGraph(time): calls for another network graph to send their transactions from a timstamp onwards. The timestamp is the last recorded timestamp in the local graph
            sendGraph(time): sends a graph from a given time to another network node

Central Bank Node (holds all ammounts and all transactions, can isue coins):
            issueCoins(address, ammount): sends coins to a given adreess, provided it does not go over the total coin count. validated by private key signature
            update(ammount): changes the ammount of coins that are in the system, allowing more coins to be issued
            burnT(symbol): burns all tokens with a symbol by changing all tokens back into the native coin, using digets specified 
            freezeT(symbol): makes sending/exchanging a token with that symbol invalid for all nodes
            burnC(ammount): burns the ammount of coins by factoring it into transaction costs for nodes. Nodes then change the transaction fee till that ammount is reached globaly
            