# set a route to display the 
#import libaraies
from flask import Flask
import json
from datetime import datetime
from block import Blockchain
from transaction import Transaction
from ledger import Ledger


app = Flask(__name__)


@app.route("/display")
def display():
    now = datetime.now()
    now = now.strftime("%m/%d/%Y, %H:%M:%S")
    column_list = ['Company Name', 'Product Name', 'Product Number', 'Unit Amount', 'Number of items','Type', 'Transaction_date']
    row_list = ['ABC Company', 'ABC Book', 'abc123', 5.00, 10, 'account receivables', now]
    my_ledger = Ledger()
    #return my_ledger.transaction_ledger(column_list, row_list)





if __name__ == "__main__":
    app.run(debug=True)