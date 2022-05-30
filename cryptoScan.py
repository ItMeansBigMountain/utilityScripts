from web3 import Web3

import websocket
import json
from pprint import pprint






# INTI SET-UP VARIABLES
SOCKET = 'wss://stream.binance.us:9443/ws/ethusdt@kline_1m'
TRADE_SYMBOL = 'ETHUSD'


# WEB SOCKET OBJECT OVERRIDE FUNCTIONS
def on_open( ws ):
    print("Opened Connection")


def on_close( ws ):
    print("closed Connection")

def on_message( ws , message):
    jsonMessage = json.loads(message)
    



# websocket object
ws = websocket.WebSocketApp(SOCKET , on_open= on_open , on_close= on_close , on_message= on_message  )
ws.run_forever()



