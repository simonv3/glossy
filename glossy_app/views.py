# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from glossy_app.dictionaries import *
from glossy_app.forms import SearchForm

def main(request):
    #search_abdv_language('Bali')
    searchForm = SearchForm(request.POST or None)
    if request.method == "POST":
        if searchForm.is_valid():
            sfCD = searchForm.cleaned_data
            wordsDict = []
            abdv_results = search_abdv_language(sfCD['language'],sfCD['query'])
            print abdv_results
            wordsDict.extend(abdv_results)
            print wordsDict
    return render_to_response("main/main_page.html", locals(),context_instance=RequestContext(request))
