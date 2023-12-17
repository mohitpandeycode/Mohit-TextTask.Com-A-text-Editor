from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')

def analyze(request):
    global prm
    djtext = request.POST.get('text','default')    # using POST in the place of GET
    removepunc = request.POST.get('removepunc', 'off')
    Capitalize = request.POST.get('capitalize', 'off')
    Dcapitalize = request.POST.get('dcapitalize', 'off')
    NewLineRemover = request.POST.get('remove', 'off')

    analyzing = ''
    punctuation = [',', '.', '!', '?', ':', ';', '-', '(', ')', '[', ']', '{', '}', '"', "'"]
    if removepunc == "on":
            for char in djtext:
                if char not in punctuation:
                    analyzing = analyzing + char
                    djtext= analyzing
            prm = {'purpose': 'Punctuation Removed', 'analyzed': analyzing}  # the dictionary

    if Capitalize == 'on' :
        analyzing=''
        for char in djtext :
                analyzing = analyzing+ char.upper()
                djtext = analyzing
        prm = {'purpose': 'Capitalize Text', 'analyzed': analyzing}  # the dictionary

    if Dcapitalize == 'on' :
        analyzing=''
        for char in djtext :
                analyzing = analyzing+ char.lower()
                djtext = analyzing
        prm = {'purpose': 'Dcapitalize Text', 'analyzed': analyzing}  # the dictionary

    if NewLineRemover == 'on' :
        analyzing=""
        for char in djtext :
            if char != "\n" and char != "\r":
                analyzing = analyzing+ char
                djtext = analyzing
        prm = {'purpose': 'New Line Removed', 'analyzed': analyzing}

    if djtext == '':
        analyzing = 'Enter the Text First....'
        prm = {'purpose': 'Text Error', 'analyzed': analyzing}
        return render(request, 'analyze.html', prm)

    if removepunc!='on' and Capitalize != 'on' and Dcapitalize != 'on' and NewLineRemover != 'on' :
        analyzing = "Please Select Any Option To Convert....!"
        prm = {'purpose': 'Option Error', 'analyzed': analyzing}
        return render(request, 'analyze.html', prm)

    else :
        return render(request, 'analyze.html', prm)  # return the dictionary also












