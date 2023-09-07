# import os
# from twilio.rest import Client



# account_sid = os.environ['AC9ff95645f4d90ba75da1577439cb3387']
# auth_token = os.environ['47975eb06128cfe56cfa272db0159046']
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="WARNING! REMOVE YOUR CAR FROM THE STATE. Otherwise get it registered for this state! ",
#                      from_='+18506603149',
#                      to='+918826927173'
#                  )
                

# print(message.sid)








import os
from twilio.rest import Client

ACCOUNT_SID = "AC9ff95645f4d90ba75da1577439cb3387"
AUTH_TOKEN = "47975eb06128cfe56cfa272db0159046"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    to="+91 8826927173", 
    #to="+91 9041756096", 
    from_="+18506603149",
    body="WARNING! REMOVE YOUR CAR WITH NUMBER PLATE XXXXXXX FROM THE STATE! OTHERWISE LEGAL ACTION WILL TAKE PLACE")

print(message.sid)