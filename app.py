from flask import Flask, request
from twilio import twiml
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def main_page():
    return "Hello Bruh!"

@app.route('/sms', methods=['POST'])
def sms():
    message_body = request.form.get('Body')
    process_text(message_body)


#-------------------------------------------------------------BOT----------------------------------------------------------------

account_sid = 'AC6d2bf720bfcfa831dae8bd2951d084b9'
auth_token = '0827fb256a3a0c6e64fa01f95c79d573'

client = Client(account_sid,auth_token)

def send(text):
    message = client.messages.create(
        body=text,
        from_='whatsapp:+14155238886',
        to='whatsapp:+919212151078'
    )

test_message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919212151078'
                          )

send("*Welcome to WHATSAPP BOT SERVICE powered by Python*")
send("_made by Saksham Bhutani_")
send("Use the following Commands to use the BOT")
send("*latest news* _to get all the top headline_")
send("*science news* _to get all top news related to science_")
send("*political news* _to get all the top news related to politics_")
send("

def process_text(input):
    if 'latest news' in input:
        NewsFromBBC()
    elif 'science news' in input:
        SciNews()
    elif 'political news' in input:
        PolNews()
    elif 'tech news' in input:
        TechNews()
    elif 'play' in input or 'youtube' in input:
        result = input.format(" ")
        result.pop(0)
        x = ""
        for i in result:
            x+=" "+i
        yt_play(x)
    elif 'search' in input or 'wikipedia' in input:
        result = input.format(" ")
        result.pop(0)
        x = ""
        for i in result:
            x+=" "+i
        search(x)
    elif 'gif' in input:
        result = input.format(" ")
        result.pop(0)
        x = ""
        for i in result:
            x+=" "+i
        giffy(x)
    elif 'joke' in input or 'tell me a joke' in input:
        joke()
    elif 'fact' in input or "tell me a fact" in input:
        fact()
    else:
        search(input)


#--------------------------------------------------------Methods-------------------------------------------------------------

def NewsFromBBC():
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=6d206038549d4806a6f204441c6dd24e"

    open_bbc_page = requests.get(main_url).json()

    article = open_bbc_page["articles"]
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(1,len(results)+1):
        send(i, results[i-1])

def SciNews():
    main_url = " https://newsapi.org/v1/articles?source=verge-news&sortBy=top&apiKey=6d206038549d4806a6f204441c6dd24e"

    open_verge_page = requests.get(main_url).json()

    article = open_verge_page["articles"]
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(1,len(results)+1):
        send(i, results[i-1])
        
def PolNews():
    main_url = " https://newsapi.org/v1/articles?source=reuterspolitical-news&sortBy=top&apiKey=6d206038549d4806a6f204441c6dd24e"

    open_reuters_page = requests.get(main_url).json()

    article = open_reuters_page["articles"]
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(1,len(results)+1):
        send(i, results[i-1])
        
def TechNews():
    main_url = " https://newsapi.org/v1/articles?source=technobus-news&sortBy=top&apiKey=6d206038549d4806a6f204441c6dd24e"

    open_technobus_page = requests.get(main_url).json()

    article = open_technobus_page["articles"]
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(1,len(results)+1):
        send(i, results[i-1])

def search(input):
    main_url= "https://api.duckduckgo.com/?skip_disambig=1&format=json&pretty=1&q="
    result = requests.get(main_url+input)
    send("*"+result['Heading']+"*")
    send(result["Abstract"])

def yt_player(input):
    main_url="https://www.youtube.com/results?search_query="
    result = requests.get(main_url+input)
    soup = BeautifulSoup(result.content,"html5")
    videos = soup.findAll("a", attrs={"class"":"yt-simple-endpoint style-scope ytd-video-renderer"})
    for video in videos:
        title = video.find("title")
        link = video.find("href")
        send("*"+title+"*")
        send(link)

def giffy(input):
    main_url="https://giphy.com/search/"
    result = requests.get(main_url+input)
    soup = BeautifulSoup(result.content,"html5")
    videos = soup.findAll("div", attrs={"class"":"sc-htoDjs cpXyQT"})
    for gif in gifs:
        link = video.find("src")
        send(link)

def joke():
    main_url = "http://api.icndb.com/jokes/random"
    result = requests.get(main_url)
    sub_result = result["value"]
    send(sub_result[joke])

def fact():
    main_url = "https://uselessfacts.jsph.pl/random/"
    result = requests.get(main_url)
    send(result[fact])

#------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run()
    
