"""
Created on Sat Jun 16 10:14:24 2018

@author: Daniel
"""

import click

@click.group()
def cli1():
    pass

@cli1.command()
@click.argument('receiver')
@click.argument('amount')
@click.argument('coinType')
def Send(receiver,amount,coinType):
    """Send Currency"""

@click.group()
def cli2():
    pass

@cli2.command()
@click.argument('symbol')
@click.argument('totalSupply')
def CreateToken(symbol, totalSupply):
    """Create New Token"""

@click.group()
def cli3():
    pass

@cli3.command()
@click.argument('amount')
def Fire(amount):
    """Delete Currency From Circulation"""

@click.group()
def cli4():
    pass

@cli4.command()
@click.argument('amount')
def Freeze(amount):
    """Freeze Tokens"""
    
@click.group()
def cli5():
    pass

@cli5.command()
@click.argument('amount')
def PlaceStake(amount):
    """Place A Stake For Minting"""

@click.group()
def cli6():
    pass

@cli6.command()
@click.argument('amount')
def RemoveStake():
    """Remove Current Stake For Minting"""
    
@click.group()
def cli7():
    pass

@cli7.command()
def checkstake():
    """Tells user if they have stake"""

cli = click.CommandCollection(sources=[cli1, cli2,cli3,cli4,cli5,cli6,cli7])

if __name__ == '__main__':
    cli()