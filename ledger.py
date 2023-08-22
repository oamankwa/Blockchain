# This model is to create an ledger object
#import libaraies
from flask import Flask
import json
from datetime import datetime
from block import Blockchain
from transaction import Transaction

# create a class for this model
class Ledger(Blockchain, Transaction):
    #create constructor
    def __init__(self):
        super().__init__()

    #add transactions to block
    def add_tranaction_block(self, column_list, row_list):
        self.Transaction_list = column_list
        trans_dict = self.add_transaction(row_list)
        s = json.dumps(trans_dict, indent=4)
        self.add_block(s)
        

    #print the ledger
    def print_ledger(self, column_list, row_list):
       self.add_tranaction_block(column_list, row_list)
       for block in self.chain:
            print('Data:', block.data)
            print('Previous hash:', block.prev_hash)
            print('Hash:', block.hash)

    #create a text file of blockchain
    def ad_ledger_text(self, path):
        new_line = '\n'
        appendblock = open(path, 'w')
        for block in self.chain:
            appendblock.write('Data: '+ block.data)
            appendblock.write(new_line)
            appendblock.write('Previous hash: '+ block.prev_hash)
            appendblock.write(new_line)
            appendblock.write('Hash: ' + block.hash)
            appendblock.write(new_line)
            appendblock.write('====================') 
            appendblock.write(new_line)
        

    #create a pdf file of blockchain
    def add_ledger_pdf(self):
        pass


now = datetime.now()
now = now.strftime("%m/%d/%Y, %H:%M:%S")
column_list = ['Company Name', 'Product Name', 'Product Number', 'Unit Amount', 'Number of items','Type', 'Transaction_date']
row_list = ['Joe Company', 'ABCF Brake', 'abc1234', 15.00, 20, 'account receivables', now]
row_list_two = ['CBAD Company', 'Dell Computer', 'cbs567', 1500.00, 10, 'account receivables', now]
my_ledger = Ledger()
my_ledger.print_ledger(column_list, row_list)
my_ledger.print_ledger(column_list, row_list_two)
my_ledger.ad_ledger_text('blockchain.txt')

