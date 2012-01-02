# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from glossy_app.dictionaries import *
from glossy_app.forms import SearchForm, LanguageForm
from glossy_app.models import Language
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required

@user_passes_test(lambda u: u.has_perm('glossy_app.can_add_language'), login_url='/admin/')
def import_austronesian(request):
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
        elif 'language' in request.POST:
            if languageForm.is_valid():
                lfCD = languageForm.cleaned_data
                abdv_results = fetch_languages(lfCD['language_query'])
                
    languageForm = LanguageForm(None)
    return render_to_response("main/main_page.html", locals(),context_instance=RequestContext(request))

def splash(request):
    languages = Language.objects.all().order_by('id').reverse()
    return render_to_response("glossy_index.html", locals(),
            context_instance=RequestContext(request))

def language(request, languageid):
    language = Language.objects.get(id = languageid)
    words = Definition.objects.filter(word__language=language).order_by('definition').extra(select={'lower_name': 'lower(definition)'}).order_by('lower_name')
    
    return render_to_response("glossy/language_page.html", locals(),
            context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    print user.first_name
    return render_to_response('glossy/profile.html', locals(),
            context_instance=RequestContext(request))
    
