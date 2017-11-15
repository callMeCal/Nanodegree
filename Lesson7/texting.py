from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa628e26516086159a89f03bcf401efde"
# Your Auth Token from twilio.com/console
auth_token  = "db5421aea2a91fd7426db5c83c26fae9"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15025171343",
    from_="+18594592085",
    body="Greetings Earthling")

print(message.sid)