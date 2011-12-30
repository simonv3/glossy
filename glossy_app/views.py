# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from glossy_app.dictionaries import *
from glossy_app.forms import SearchForm, LanguageForm
from glossy_app.models import Language

def main(request):
    #search_abdv_language('Bali')
    languageForm = LanguageForm(request.POST or None)
    searchForm = SearchForm(request.POST or None)
    languages = Language.objects.all()
    if request.method == "POST":
        if 'word' in request.POST:
            if searchForm.is_valid():
                sfCD = searchForm.cleaned_data
                wordsDict = []
                abdv_results = search_abdv_language(sfCD['language'],sfCD['query'])
                wordsDict.extend(abdv_results)
                print wordsDict
        elif 'language' in request.POST:
            print "searching languages"
            if languageForm.is_valid():
                lfCD = languageForm.cleaned_data
                

    return render_to_response("main/main_page.html", locals(),context_instance=RequestContext(request))

def splash(request):
    languages = Language.objects.all()
    return render_to_response("glossy_index.html", locals(),
            context_instance=RequestContext(request))

def language(request, languageid):
    language = Language.objects.get(id = languageid)
    return render_to_response("glossy/language_page.html", locals(),
            context_instance=RequestContext(request))
    
