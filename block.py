# These models are blockchain with a qr-code
#import libaraies
from flask import Flask
import hashlib

# create a block class
class Block:
    #create variables
    data = []

    #create a constructor
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    # method calculate hash using SHA-256
    def calc_hash(self):
        sha = hashlib.sha224()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()
    
#create the blockchain class
class Blockchain:
    #add a constructor
    def __init__(self):
        self.chain = [self.genesis_block()]

    #method create the first block
    def genesis_block(self):
        return Block("Genesis Block", "0")
    
    #add a block to the chain
    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(data, prev_block.hash)
        self.chain.append(new_block)






