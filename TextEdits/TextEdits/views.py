from email.policy import default
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    
    return render(request,'index.html')

def analyze(request):
     # getting the text and storing it in the variable
    djtext = request.POST.get('text', 'default')
    # checking the switches and storing them in variables
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    # if functions to perform eash tasks
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Punctuations Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if capitalize == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized All', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremove == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Newline Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremove == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spaced Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == 'on':
        analyzed = ''
        strtype = str(len(djtext))
        analyzed = analyzed + strtype
        params = {'purpose': 'Character Counted', 'analyzed_text': analyzed}

    if (removepunc != 'on' and capitalize != 'on' and newlineremove != 'on' and spaceremove != 'on' and charcount != 'on'):
        return render(request, 'error.html')

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
