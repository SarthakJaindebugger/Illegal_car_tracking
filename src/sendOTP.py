import os
from twilio.rest import Client

def otp_send():
    ACCOUNT_SID = "AC9ff95645f4d90ba75da1577439cb3387"
    AUTH_TOKEN = "47975eb06128cfe56cfa272db0159046"

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        to="+91 8826927173", 
        from_="+18506603149",
        body="WARNING! REMOVE YOUR CAR WITH NUMBER PLATE XXXXXXX FROM THE STATE! OTHERWISE LEGAL ACTION WILL TAKE PLACE.")

    print("Message sent, with sid : ",message.sid)


# otp_send()