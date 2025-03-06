import requests
from bs4 import BeautifulSoup as bs
from gtts import gTTS
from playsound import playsound
import os

# User-Agent and Language settings for the request
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
LANGUAGE = "en-US, en;q=0.5"

# Initialize the session with headers
session = requests.Session()
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE

# User input for the type of news
x = input("Enter news type (e.g., 'india', 'world', 'technology'): ")
url = "https://www.hindustantimes.com/" + x

# Request and parse the HTML content
html = session.get(url)
soup = bs(html.text, "html.parser")

# Extracting news headlines
a = soup.find_all("h3", attrs={"class": "hdg3"})
print("Today's headlines:")

# Combine headlines into a single string for TTS
news_text = ""
for ele in a:
    b = ele.text.strip()
    news_text += b + ". "  # Add period and space for better TTS reading
    print(b)

# Convert the news text to speech
if news_text:
    obj = gTTS(text=news_text, lang='en', slow=False)
    obj.save("news.mp3")
    playsound("news.mp3")
    os.remove("news.mp3")
else:
    print("No headlines found. Please check the news type or website structure.")