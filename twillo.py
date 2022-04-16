from twilio.rest import Client
account_sid = ''
auth_token = ''

import datetime

import os
from flask import Flask , request , redirect
from twilio.twiml.messaging_response import MessagingResponse





app = Flask(__name__)




@app.route("/sms" , methods = ['/GET' , 'POST'] )
def sms_reply():
    resp = MessagingResponse()
    resp.message("did this work")
    return str(resp)



def sendText(input_message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=input_message,from_='+',to='')
    print(message.body)




if __name__ == "__main__":
    app.run(debug=True)
