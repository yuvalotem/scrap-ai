import requests
from bs4 import BeautifulSoup
import sys
import google.generativeai as genai

words = sys.argv[1:]
capitalized_words = [word.capitalize() for word in words]
converted_sentence = '_'.join(capitalized_words)

url = 'https://en.wikipedia.org/wiki/' + converted_sentence
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

paragraphs = soup.find_all('p')

content = ''
for p in paragraphs:
    text = p.get_text()
    content += text


secret = '<your_google_ai_secert>'
genai.configure(api_key=secret)
model = genai.GenerativeModel('gemini-pro')
prompt = 'Recape this text into 3 short and simple sentences - ' + content
gemeniResponse = model.generate_content(prompt)
print(gemeniResponse._result.candidates[0].content.parts[0].text)

