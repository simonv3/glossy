from BeautifulSoup import BeautifulStoneSoup
import urllib

languageDict = {"Bali":1,"Banggai":2,"Banggi":3,"Banggi":4}

def fetch_abdv_languages():
    return "hello"

def search_abdv_language(language, query):
    #print language
    ABDVlangs = range(0,5) #these languages are the abdv languages
    #print ABDVlangs
    if int(language) in ABDVlangs:
        params = urllib.urlencode({'language': 1, 'type': 'xml', 'section':
            'austronesian'})
        f = urllib.urlopen("http://language.psy.auckland.ac.nz/utils/save/index.php?%s" % params)
        soup = BeautifulStoneSoup(f.read())
        recordsList = []
        for record in soup('record'):
            if record('word'):
                if record('word')[0].contents[0] == query:
                    recordDict={"definition":record('word')[0].contents[0],"word":record('item')[0].contents[0]}
                    recordsList.append(recordDict)
        return recordsList
            #print recordSoup
            #if recordSoup('item').string == query: print "true"
#          print recordSoup
#            if recordSoup('item').string == query: print "true"
    pass
    

