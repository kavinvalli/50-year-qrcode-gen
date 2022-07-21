from twilio.rest import Client

account_sid = 'AC42f446ae9255bf244378a329d76991a3'
auth_token = '[Redacted]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Your Twilio code is 1238432',
    to='whatsapp:+917701822620'
)

print(message.sid)
