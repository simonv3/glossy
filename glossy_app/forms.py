from django import forms

languageDict = [('1',"Bali"),('2',"Banggai"),('3',"Banggi"),('4',"Banggi")]

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    language = forms.ChoiceField(choices=languageDict)

class LanguageForm(forms.Form):
    language_query = forms.CharField(max_length=100)

class LanguageCommentForm(forms.Form):
    author_name = forms.CharField(max_length=200)
    author_email = forms.EmailField(max_length=200)
    author_id = forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea)

