import requests,random,re
from flask import Flask ,render_template,request

app = Flask(__name__)
@app.route("/",methods=['GET', 'POST'])
def home():
	import requests,random,re
	main_list={"all":"https://inshorts.vercel.app/all","national":"https://inshorts.vercel.app/national",
	           "buisness":"https://inshorts.vercel.app/business","sports":"https://inshorts.vercel.app/sports",
	           "world":"https://inshorts.vercel.app/world","politics":"https://inshorts.vercel.app/politics",
	           "technology":"https://inshorts.vercel.app/technology","startup":"https://inshorts.vercel.app/startup",
	           "entertainment":"https://inshorts.vercel.app/entertainment",
	           "science":"https://inshorts.vercel.app/science","automobile":"https://inshorts.vercel.app/automobile"}
	tag=['all', 'national', 'buisness', 'sports', 'world', 'politics', 'technology', 'startup', 'entertainment',
	     'science', 'automobile']
	main_list_selection=random.choice([i for i in range(0,11)])
	url=main_list[tag[main_list_selection]]
	data=requests.get(url).json()
	news_selection=random.choice([i for i in range(0,len(data['articles']))])
	news=data['articles'][news_selection]
	news['title']=re.sub(' +', ' ', news['title'])[1:-1:1]
	news['tag']=tag[main_list_selection]
	return render_template('index.html',news=news)

app.run(debug=True)