import twitter, datetime, time
import urllib, urllib2

while True:
    #read currentSession
    currentSession = open("/Users/farasuhaili/Library/Application Support/Google/Chrome/Default/Current Session")
    lastSession = currentSession.read()

    #user twitter ID
    user = 529357749
    file = open("APITweet.txt")
    cred = file.readline().strip().split(',')

    #twitter API
    api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])
 

    #find the latest URL
    startIndex = lastSession.rfind("http")
    endIndex = lastSession.find(chr(0), startIndex)
    url = lastSession[startIndex:endIndex]
    print(url)

    
    #get title
    readhtml = urllib2.urlopen(url)
    thePage = readhtml.read()
    theTitle = thePage[thePage.index('<title'):thePage.index('</title>')]
    theTitle = theTitle.replace('<title>','')
    print("The title is : " + theTitle.strip())
    print("I'm really liking " + theTitle.strip() + " on " + url)

    #post twitter
    timestamp = datetime.datetime.utcnow()
    response = api.PostUpdate("I'm really liking " + theTitle.strip() + " on " + url)
    print("Tweeted!")
    #response = api.PostUpdate("Tweeted at " + str(timestamp))
    #statuses = api.GetUserTimeLine(user)
    #print (statuses[0].text)

    time.sleep(3600)
