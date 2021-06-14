import re
import requests
import xml.etree.ElementTree as ET

# feed = requests.get('https://netcan.github.io/atom.xml').text
feed = requests.get('https://jackyc.cn/atom.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(r'''
```

   ___               _               _____ 
  |_  |             | |             /  __ \
    | |  __ _   ___ | | __ _   _    | /  \/
    | | / _` | / __|| |/ /| | | |   | |    
/\__/ /| (_| || (__ |   < | |_| | _ | \__/\
\____/  \__,_| \___||_|\_\ \__, |(_) \____/
                            __/ |          
                           |___/           

```
''')

#     f.write(r'''
# ## Latest talks
# ''')
#     talks = requests.get('https://raw.githubusercontent.com/netcan/presentation/master/README.md').text
#     for (topic, url) in re.findall('- (.*): (.*)', talks)[:5]:
#         f.write('- [{}]({})\n'.format(topic, url))

    f.write(r'''
## Latest blog posts
''')
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        # print(text)
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        # print(url)
        published = entry.find('nsfeed:published', nsfeed).text[:10]
        # print(published)
        # print('==================================')
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('''
[>>> More blog posts](https://netcan.github.io/archives/)


## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=SCNUJackyChen)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=SCNUJackyChen&hide=ipynb,html&layout=compact)
''')