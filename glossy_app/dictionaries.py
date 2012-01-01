from BeautifulSoup import BeautifulStoneSoup
import urllib
from glossy_app.models import *

def fetch_abdv_languages():
    return "hello"

def search_abdv_language(language, query):
    #print language
    ABDVlangs = range(0,5) #these languages are the abdv languages
    #print ABDVlangs
    if int(language) in ABDVlangs:
        params = urllib.urlencode({'language': language, 'type': 'xml', 'section':
            'austronesian'})
        print params
        f = urllib.urlopen("http://language.psy.auckland.ac.nz/utils/save/index.php?%s" % params)
        soup = BeautifulStoneSoup(f.read())
        recordsList = []
        for record in soup('record'):
            if record('word'):
                if record('word')[0].contents[0] == query:
                    recordDict={"definition":record('word')[0].contents[0],"word":record('item')[0].contents[0]}
                    recordsList.append(recordDict)
        print recordsList
        return recordsList
            #print recordSoup
            #if recordSoup('item').string == query: print "true"
#          print recordSoup
#            if recordSoup('item').string == query: print "true"
    pass

def fetch_languages(language):
    params = urllib.urlencode({'language':language , 'type':'xml', 'section':'austronesian'})
    url = "http://language.psy.auckland.ac.nz/utils/save/index.php?%s" % params
    f = urllib.urlopen(url)
    recordsList = []
    soup = BeautifulStoneSoup(f.read())
    print soup('record')[0]('language')
    language = soup('record')[0]('language')[0].contents[0]
    print language
    author = soup('record')[0]('author')[0].contents[0]
    silcode = soup('record')[0]('silcode')[0].contents[0]
    try:
        notes = soup('record')[0]('notes')[0].contents[0]
    except:
        notes = ""
    new_language = Language(language = language, author = author, silcode =
                silcode, notes = 'notes: ' + notes,
                resources = url)
    new_language.save()
    
    for record in soup('record'):
            if record('word'):
                try:
                    annotation = record('annotation')[0].contents[0]
                except:
                    annotation = ""
    
                recordDict={"definition":record('word')[0].contents[0],"word":record('item')[0].contents[0], "annotation":annotation}
                print recordDict
                word = Word(word = recordDict["word"], language = new_language)
                word.save()
                definition = Definition(word = word, definition = recordDict["definition"], annotations = recordDict["annotation"])
                definition.save()
    
    
    return recordsList

