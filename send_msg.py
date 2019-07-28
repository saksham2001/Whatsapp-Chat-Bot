from twilio.rest import Client
import webhook

account_sid = 'AC6d2bf720bfcfa831dae8bd2951d084b9'
auth_token = '0827fb256a3a0c6e64fa01f95c79d573'

client = Client(account_sid,auth_token)

from_whatsapp_number = "whatsapp:+919212151078"
to_whatsapp_number ="whatsapp:+14155238886"


intro = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919212151078'
                          )


def send(text):
    message = client.messages.create(
        body=text,
        from_='whatsapp:+14155238886',
        to='whatsapp:+919212151078'
    )



def process_text(input):
    if 'latest news' in input:
        NewsFromBBC()
    else:
      pass

def NewsFromBBC():
            main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=6d206038549d4806a6f204441c6dd24e"

            open_bbc_page = requests.get(main_url).json()

            article = open_bbc_page["articles"]
            results = []

            for ar in article:
                results.append(ar["title"])

            for i in range(1,len(results)+1):
                send(i, results[i-1])
                
if __name__=="__main__":
  process_text(message_body)
