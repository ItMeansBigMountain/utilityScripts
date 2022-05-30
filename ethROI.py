import websocket
import json
from pprint import pprint
import talib
import numpy




# PAPER TRADING ROI AVG 



# STREAMING CRYPTO TICKER DATA
SOCKET = 'wss://stream.binance.us:9443/ws/ethusdt@kline_1m'
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'ETHUSD'
TRADE_QUANTITY = 0.05



HOLD_AMOUNT = 0




closes = []
in_position = False


def on_open( ws ):
    print("Opened Connection")


def on_close( ws ):
    print("closed Connection")


def on_message( ws , message):
    global closes
    print(f'\t current amount:  ${HOLD_AMOUNT} ')

    jsonMessage = json.loads(message)
    candle = jsonMessage['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append( float(close) )
        print("---all closes---")
        print(closes)


        # calculate rsi using ta-lib
        if len(closes) > RSI_PERIOD :
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes , RSI_PERIOD)
            print("\nrsi")
            print(rsi)
            last_rsi = rsi[-1]
            print(last_rsi)

            # SELL
            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print('\nOVERBOUGHT - sell!!!!')
                    HOLD_AMOUNT -= TRADE_QUANTITY * last_rsi
                    in_position = False
                else:
                    print("\OVERBOUGHT - you dont any... nothing to do")

            # BUY
            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("\nOVERSOLD -  but you own it... nothing to do ")
                else:
                    print('\nOVERSOLD - buy buy buy!')
                    HOLD_AMOUNT -= TRADE_QUANTITY * last_rsi
                    HOLD_AMOUNT += closes[-1]
                    in_position = True










# runs a loop where we get a stream onf constant data from binance
ws = websocket.WebSocketApp(SOCKET , on_open= on_open , on_close= on_close , on_message= on_message  )
ws.run_forever()



