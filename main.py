import requests,random,re
from flask import Flask ,render_template,request

app = Flask(__name__)
@app.route("/",methods=['GET', 'POST'])
def home():
	base_url="https://inshorts.vercel.app/news?category="
	tag=['all', 'national', 'business', 'sports', 'world', 'politics', 'technology', 'startup', 'entertainment',
	     'science', 'automobile']
	main_list_selection=random.choice([i for i in range(0,11)])
	url=base_url+tag[main_list_selection]
	print(url)
	data=requests.get(url).json()
	news_selection=random.choice([i for i in range(0,data['total'])])
	news=data['articles'][news_selection]
	news['title']=re.sub(' +', ' ', news['title'])[1:-1:1]
	news['tag']=tag[main_list_selection]
	return render_template('index.html',news=news)

if __name__ == "__main__":
    #app.debug = True
    app.run()
