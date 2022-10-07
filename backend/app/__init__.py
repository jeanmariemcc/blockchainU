from flask import Flask

from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)


@app.route('/')
def default():
    return 'Welcome to the blockchain project Yeah!'


app.run()
