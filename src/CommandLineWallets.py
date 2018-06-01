# -*- coding: utf-8 -*-
"""
Created on Fri May 25 20:44:42 2018

Currently Using Click for CLI, still figuring it out.

@author: Daniel
"""
import click

@click.command()
@click.argument('reciver')
@click.argument('amount')
@click.Option('--type', '-t',default=BinanceCoin,help = 'Type of Coin or Token to send')
def transfer(ammount, address):
        print(reciver + ' recived' + amount + ' of' + --type)
