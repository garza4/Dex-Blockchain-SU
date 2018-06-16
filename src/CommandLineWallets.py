# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 10:14:24 2018

@author: Daniel
"""
import click

@click.group('receiver','amount','coinType')
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
def CreateToken():
    """Create New Token"""

@click.group()
def cli3():
    pass

@cli3.command()
def Fire():
    """Delete Currency From Circulation"""

@click.group()
def cli4():
    pass

@cli4.command()
def Freeze():
    """Freeze Tokens"""
    
@click.group()
def cli5():
    pass

@cli5.command()
def PlaceStake():
    """Place A Stake For Minting"""

@click.group()
def cli6():
    pass

@cli6.command()
def RemoveStake():
    """Remove Current Stake For Minting"""

cli = click.CommandCollection(sources=[cli1, cli2,cli3,cli4,cli5,cli6])

if __name__ == '__main__':
    cli()