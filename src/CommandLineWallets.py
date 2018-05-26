# -*- coding: utf-8 -*-
"""
Created on Fri May 25 20:44:42 2018

Currently Using Click for CLI, still figuring it out. 

@author: Daniel
"""
import click

@click.command()
@click.Option('--address', default = None, help = 'this is the address that will recive coins' )

@click.Option('--ammount', default = 0, help = 'the ammount to be sent' )

def transfer(ammount, address):
        print(ammount + 'sent to ' + address)
        
    
