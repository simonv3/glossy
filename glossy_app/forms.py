from django import forms

languageDict = [('1',"Bali"),('2',"Banggai"),('3',"Banggi"),('4',"Banggi")]

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    language = forms.ChoiceField(choices=languageDict)

