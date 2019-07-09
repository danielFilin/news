from bottle import route, run, template, error, static_file, request
import json
import feedparser

feed = feedparser.parse("https://www.jpost.com/Rss/RssFeedsHeadlines.aspx")
title = []
link = []


for i in range(10):
    title.append(feed["entries"][i]["title"])
    link.append(feed["entries"][i]["link"])


    thisdict =	{
  "news": title,
  "link": link
}
    

@route('/', method='GET')
def index():
    return template("ex2.html")

@route('/showNews', method='GET')
def showNews():
        return json.dumps(thisdict)

@route('/newsFeed', method='POST')
def newsFeed():
    my_feed = request.POST.get("news")
    print(my_feed)
    

@error(404)
def not_found(error):
    return template("exerror.html")


@route('<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')

def main():
    run(host='localhost', port=7001)


if __name__ == '__main__':
    main()

