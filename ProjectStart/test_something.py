import requests
import re

html = requests.get('https://item.jd.com/5025518.html')
with open('a.html', 'wb') as f:
    f.write(html.content)


