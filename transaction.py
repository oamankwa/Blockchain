# This model is to create a transaction object
#import libaraies
from flask import Flask
from datetime import datetime
import csv

# create a class for this model
class Transaction:
    #add variables
    Transaction_list = []
   
    #create a constructor
    def __init__(self, trans_list):
        self.Transaction_list = trans_list
        

    #add transaction so that list_length should be the same as Transaction list
    def add_transaction(self, list_two):
        dictionary = {k: v for k, v in zip(self.Transaction_list, list_two)}
        return dictionary


    #add transactions from csv file
    def bulk_transactions(self, path):
        with open(path) as f:
            csvfile = csv.reader(f, delimiter=',')
            for row in csvfile:
                dictionaries = {self.add_transaction(row)}
            return dictionaries
            
            






