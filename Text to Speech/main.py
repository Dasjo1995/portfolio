import requests
import os
import wave
from PyPDF2 import PdfReader        #pip install PyPDF2

#API_KEY = "c421a12ccf734689bcdc6b5e3e6fe636"

API_KEY = os.environ["API_KEY"]
print(API_KEY)

reader = PdfReader('pdf-test.pdf')
# printing number of pages in pdf file:
#print(len(reader.pages)), can make for loop going through each page in this range
page = reader.pages[0]
text = page.extract_text()
print(text)

SRC = text

parameters = {
    "key": API_KEY,
    "hl": "en-gb",
    "src": SRC,
}

response = requests.get("https://api.voicerss.org/?", params=parameters)
response.raise_for_status()

print(response.content)
with open('myfile.wav', mode='bx') as f:
    f.write(response.content)




