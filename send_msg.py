import os
from twilio.rest import Client
import webhook




account_sid = 'AC6d2bf720bfcfa831dae8bd2951d084b9'
auth_token = '0827fb256a3a0c6e64fa01f95c79d573'

client = Client(account_sid,auth_token)

from_whatsapp_number = "whatsapp:+919212151078"
to_whatsapp_number ="whatsapp:+14155238886"


message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919212151078'
                          )
