# my test chatbox
import urllib
import urllib2

file = open("stop-words.txt")
stopwords = file.readlines()

def removeStopwords (message):
    for word in stopwords:
        next = word.strip()
        message = message.replace(" " + next + " ","")
        next = next.title()
        message = message.replace(" " + next + " ","")
    return message


def removemarkup(text):
    tag = False
    quote = False
    out = ""
 
    for c in text:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif c == '[' and not quote:
                tag = True
            elif c == ']' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c
    return out


while True:
    #Question1
    inputtext = raw_input("ZAARA: Hello, what is your name?")
    inputtext = " " + inputtext + " "
    varname = removeStopwords(inputtext)
    varname = varname.replace("name","")
    print("Your filtered text was: " + varname.strip())

    #Question2
    input = raw_input("ZAARA: How are you today " + varname.strip() + "?")
    filtered = " " + input + " "
    filtered = removeStopwords(filtered)
    filtered = filtered.replace("today","")
    filtered = filtered.replace("feeling","")
    filtered = filtered.replace("well","")
    vartoday = filtered.strip()
    #print vartoday
    if vartoday == 'fine' :
        print ("ZAARA: Thats good")
    elif vartoday == "not" :
        print ("ZAARA: oh, pity you")
    else:
        print ("ZAARA: oh,okay")
 
    #Question3
    inputtext = raw_input("ZAARA: Are you married?")
    inputtext = " " + inputtext + " "
    filtered = removeStopwords(inputtext)
    varMarried = filtered.replace("married","")
    varMarried = varMarried.strip()
    #print varMarried
    if varMarried == 'yes' :
        print ("ZAARA: Oh, lucky you" )
    elif varMarried == 'no' :
        print ("ZAARA: Wow,thats cool!")
    else:
        print ("ZAARA: oh,great")

    #Question4
    inputtext = raw_input("ZAARA: What do you want me to search for you " + varname.strip() + " ?")
    searchword = inputtext
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request('http://en.wikipedia.org/wiki/' + searchword.strip(),headers=hdr)
    response = urllib2.urlopen(req)
    the_page = response.read()
    the_page = the_page[the_page.index('<p>'):the_page.index('</p>')]
    the_pagestring = removemarkup(the_page)
    print(the_pagestring.strip())
