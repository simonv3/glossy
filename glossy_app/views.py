# Create your views here.
from django.shortcuts import render_to_response


def main(request):
    return render_to_response("main/main_page.html")
