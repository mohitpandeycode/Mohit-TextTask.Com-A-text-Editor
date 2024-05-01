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

    if djtext == "Anjali Mehta" or djtext == "anjali mehta" or djtext == "Anjali mehta" :
        analyzing="Hey Anjali my baby😋, just wanted to take a moment to remind you of how special you are to me. Your smile brightens my day, your laughter is music to my ears, and your presence fills my heart with warmth and joy. I feel incredibly lucky to have you in my life, and I cherish every moment we spend together. You mean the world to me, and I'm so grateful to have you as my girlfriend. Sending you all my love and a sweet hug from afar. 💖I love you baby🥰😍❤️"
        djtext = analyzing
        prm = {'analyzed': analyzing}

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

    if removepunc!='on' and Capitalize != 'on' and Dcapitalize != 'on' and NewLineRemover != 'on':
        analyzing = "Please Select Any Option To Convert....!"
        prm = {'purpose': 'Option Error', 'analyzed': analyzing}
        return render(request, 'analyze.html', prm)

    else :
        return render(request, 'analyze.html', prm)  # return the dictionary also












